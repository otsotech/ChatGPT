import requests
import json

while True:
    message = str(input('Message: '))
    def get_response(text, lang):
        params = {'text': text, 'lang': lang}
        response = requests.get('https://api.pawan.krd/chat/gpt', params=params)
        return response.json()
    response = get_response(message, 'en')
    print(response['reply'])