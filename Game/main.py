from itsdangerous import json
import requests
from os import system

SERVER_IP = '127.0.0.1'
SERVER_URL = f'http://{SERVER_IP}:5000/'

def main():
    print('Приветсвуем в игре')
    if input('Желаете подключиться (Y/N): ') == 'Y':
        resp = requests.post(f'{SERVER_URL}connect', json={'name': input('Ваш ник: ')})
        print(resp.json()['status'])


if __name__ == '__main__':
    main()