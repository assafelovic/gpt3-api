# -*- encoding: utf-8 -*-
import os

'''
    Flask API server configuration
'''
DEBUG = True
PORT = 5005
HOST = '127.0.0.1'

'''
    OpenAI GPT configuration
    For security purposes, set OpenAI API Key in root folder .env file
'''
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GPT_MODEL = 'text-davinci-003'
TEMPERATURE = 0.7
MAX_TOKENS = 80

