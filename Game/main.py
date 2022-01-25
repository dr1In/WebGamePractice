import requests
from os import system

SERVER_IP = '127.0.0.1'
SERVER_URL = f'http://{SERVER_IP}:5000/'

def main():
    print('Status: ON')
    print('Просмотр открытых лобби - 1')
    print('Стать хостом - 2')
    if input() == 1:
        system('CLS')
        lobby_checher()

def lobby_checher():
    pass


if __name__ == '__main__':
    main()