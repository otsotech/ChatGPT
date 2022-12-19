import requests
import json

def get_response(text, lang):
    params = {'text': text, 'lang': lang}
    response = requests.get('https://api.pawan.krd/chat/gpt', params=params)
    return response.json()

while True:
    message = input('Message: ')  # str() is not necessary here
    response = get_response(message, 'en')
    print(response['reply'])
