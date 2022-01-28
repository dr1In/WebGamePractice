import requests
from os import system

from main import SERVER_URL


def Lobby_creation(username):
    while True:
        resp  = requests.post(f'{SERVER_URL}create_lobby', json = {
            'name': input('Название лобби: '),
            'max': input('Кол-во игроков: '),
            'user': username
        })
        if resp.json()['status'] == 'ok':
            print('Лобби созданно')
            break
        else:
            print('Название занято')


def Lobby_connection(username):
    resp = requests.get(f'{SERVER_URL}lobbies')
    for lobby in resp.json()['lobbies']:
        print(lobby['lobby_name'] + ':', lobby['max'])
    while True:
        cur_lobby = input('Для подключения введите название лобби: ')
        to_connect = requests.post(f'{SERVER_URL}lobby_connect', json={
            'name': cur_lobby,
            'user': username
        })
        if to_connect.json()['status'] == 'ok':
            print('Вы подключились')
            break
        else:
            print('Лобби уже переполненно')
        

def Lobby_show(username):
    system('CLS')
    print("Вы подключенны")
    print("Игроки:")
    
    status_storage = list()
    players_status = requests.get(f'{SERVER_URL}lobby_info')
    (num, size) = (1, int(players_status.json()['size']))
    for name in players_status.json()['status'].keys():
        print(name + ':', players_status.json()['status'][name])
        status_storage.append(players_status.json()['status'][name])
        num += 1
    for i in range(num, size + 1):
        print('Игрок отсутсвует')
    if players_status.json()['status'][username] == 'Not ready':
        print('\n' + 'Вы не готовы введите /Ready')
        return True
    elif 'Not ready' in status_storage:
        return True
    else:
        return False
    


def Lobby_coms(com):
    if com == '/Ready':
        resp = requests.post(f'{SERVER_URL}make_ready')
        return resp.json()['answer']