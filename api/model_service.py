# -*- encoding: utf-8 -*-
from api.config import OPENAI_API_KEY, TEMPERATURE, MAX_TOKENS, GPT_MODEL
import openai


class ModelService:

    def __init__(self):
        openai.api_key = OPENAI_API_KEY

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
            core openai wrapper for completion API
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
        return result
