# -*- encoding: utf-8 -*-
import openai

from api.config import OPENAI_API_KEY, TEMPERATURE, MAX_TOKENS, GPT_MODEL


class ModelService:

    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    '''
        The moderation endpoint is a tool you can use to check whether content is harmful and complies with OpenAI's usage policies.
    '''
    def moderation(self, input):
        r = openai.Moderation.create(
            input=input
        )
        return r


    """
        core openai wrapper for completion API
    """
    def completion(self, prompt, kwargs={}):
        temp = kwargs.setdefault('temperature', TEMPERATURE)
        max_tokens = kwargs.setdefault('max_tokens', MAX_TOKENS)
        model = kwargs.setdefault('model', GPT_MODEL)

        r = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=temp,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return {
            "result": r["choices"][0]["text"].strip(),
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temp
        }

    """
        API Wrapper for ChatGPT
    """
    def chat(self, kwargs={}):
        # Assume the following format: [{'role':'assistant'/'user', 'content': '...'},...]
        messages = kwargs.get("messages")

        # (Optional) The chat_behavior is a system message that helps set the behavior of the assistant.
        chat_behavior = kwargs.get("chat_behavior")
        if chat_behavior:
            messages.insert(0, {"role": "system", "content": chat_behavior})

        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        completion_response = r["choices"][0]["message"]["content"].rstrip()
        return completion_response

    """
       API Wrapper for OpenAI Whisper
    """
    def transcribe(self, kwargs={}):
        audio_path = kwargs.get("audio_path")
        file = open(audio_path, "rb")
        transcription = openai.Audio.transcribe("whisper-1", file)
        return transcription

    """
        API Wrapper for Dalle 2
        Please note, images returned as uri will be removed within 1 hour.
    """
    def image(self, prompt, kwargs={}):
        n = kwargs.setdefault('n', 1)
        size = kwargs.setdefault('size', '512x512')

        r = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )

        return {
            "url": r["data"][0]["url"],
            "n": n,
            "size": size
        }

    """
        API Wrapper for prompt completion
    """
    def predict(self, prompt, kwargs={}):
        result = self.completion(prompt, kwargs)
        if kwargs.get("moderation"):
            moderation_results = self.moderation(result.get("result"))
            result["moderation"] = moderation_results
        return result

