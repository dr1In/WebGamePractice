import requests
from os import system

from main import SERVER_URL


def Lobby_creation(username):
    while True:
        resp  = requests.post(f'{SERVER_URL}create_lobby', json = {
            'name': input('Название лобби: '),
            'max': input('Кол-во игроков (мин - 2): '),
            'month': input('Кол-во месяцев или 0 (пока все не банкроты): '),
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
        print(lobby['lobby_name'] + ':', lobby['max'], lobby['type'])
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
    return cur_lobby
        

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


def game_connect(username, g_id):
    resp = requests.post(f'{SERVER_URL}connect', json={
        'id': g_id,
        'user': username
    })


def info():
    resp = requests.get(f'{SERVER_URL}get_info')
    print('Предложений сырья:', resp.json()['material_quantity'])
    print('Минимальная цена сырья:', resp.json()['material_cost'], 'т.р.')
    print('Спрос на истребители:', resp.json()['plane_quantity'])
    print('Максимальная цена за истребитель:', resp.json()['plane_cost'], 'т.р.')