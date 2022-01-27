import requests

api_token = '1862933682:AAE4bucIW6lD4-pX_Qmr-wZFJSuNE1j-qZg'


def send():
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        chat_id=456899553,
        text='Connect Error!'
    ))


'''
если бот не работает, то через BotFather нодо получить новый токен
https://api.telegram.org/bot1862933682:AAE4bucIW6lD4-pX_Qmr-wZFJSuNE1j-qZg/getUpdates

1862933682:AAE4bucIW6lD4-pX_Qmr-wZFJSuNE1j-qZg

456899553
'''

# send()
