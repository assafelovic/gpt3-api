# OpenAI Flask API Wrapper

A basic Flask API interface for OpenAI GPT3, ChatGPT, Whisper and Dalle2 including training and examples.

<br />

> Features:

- Simple, intuitive codebase - can be extended with ease. 
- `Gunicorn` support
- `Docker` support
- Includes both prediction and training GPT3 services


## API

| Route  | Method | Info | 
|    --- | ---  | --- | 
| `/` | **GET**    | Get current GPT3 model params
| `/api/v1/predict`    | **POST**    | Predict GPT3 prompt completion
| `/api/v1/image`    | **POST**    | Generate Dalle-2 prompt image
| `/api/v1/chat`    | **POST**    | ChatGPT wrapper including context support
| `/api/v1/transcribe`    | **POST**    | OpenAI Whisper Transcription

<br />

> **Before you run** - Set your OpenAI API Key in .env file

```bash
$ echo 'API_KEY={Your key here}' .env
```

<br />

## Quick Start with Docker


```bash
$ git clone https://github.com/assafelovic/gpt3-api.git
$ cd gpt3-api
```

```bash
$ docker-compose up --build  
```

The API server will start using the PORT `5005`. 

<br />

## Usage example
Client sends post request with the params `prompts` (String) and optional params to  `http://127.0.0.1:5005/api/v1/predict`
```
POST /api/v1/predict
{
  prompt: "What is the meaning of life?",
  max_tokens: 128, 
  temperature: 0.4
}
```

and the server responds with the predicted result:

```
{
    "result": {
        "max_tokens": 128,
        "model": "text-davinci-002",
        "result": "There is no one answer to this question. To some people, life might mean spending time with family, others might believe that the meaning of life is to help others.",
        "temperature": 0.4
    },
    "success": true
}
```

## Installation

> **Step #1** - Clone the project

```bash
$ git clone https://github.com/assafelovic/gpt3-api.git
$ cd gpt3-api
```

<br />

> **Step #2** - Install dependencies
```bash
$ pip install -r requirements.txt
```
<br />

> **Step #3** - setup `flask` command for our app

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```
<br />

> **Step #4** - start development server at `localhost:5005`

```bash
$ flask run
```


---