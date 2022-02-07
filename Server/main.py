from flask import Flask, jsonify, request

from Server_utils import Game, Player, Lobby


app = Flask(__name__)


lobbies_list = dict()
users_ip_lobby = dict()


game = Game()


@app.post('/create_lobby')
def create_lobby():
    name_lobby = request.json['name']
    max_players = request.json['max']
    username = request.json['user']
    ip = request.remote_addr
    users_ip_lobby[ip] = name_lobby

    if name_lobby not in lobbies_list:
        lobbies_list[name_lobby] = Lobby(name_lobby, max_players)
        lobbies_list[name_lobby].connect(username, ip)
        return jsonify(status = 'ok')
    else:
        return jsonify(status = 'name exception')


@app.get('/lobbies')
def lobbies():
    information = [{
        'lobby_name': _,
        'max': lobbies_list[_].get_emptiness()
    } for _ in lobbies_list.keys()]
    return jsonify(lobbies = information)


@app.get('/lobby_info')
def lobby_info():
    ip = request.remote_addr
    return jsonify(
        status = lobbies_list[users_ip_lobby[ip]].get_players_status(),
        size = lobbies_list[users_ip_lobby[ip]].get_max()
    )


@app.post('/lobby_connect')
def lobby_connect():
    name_lobby = request.json['name']
    username = request.json['user']
    ip = request.remote_addr
    users_ip_lobby[ip] = name_lobby
    if lobbies_list[name_lobby].connect(username, ip):
        return jsonify(status = 'ok')
    else:
        return jsonify(status = 'lobby full')


@app.post('/make_ready')
def make_ready():
    ip = request.remote_addr
    lobbies_list[users_ip_lobby[ip]].player_ready(ip)
    return jsonify(answer = 'Вы готовы, ожидание других')


@app.get('/get_info')
def get_info():
    pass


@app.post('/buy_raw')
def buy_raw():
    pass


@app.post('/sell_planes')
def sell_planes():
    pass


@app.post('/produce')
def produce():
    pass


@app.post('/build')
def build():
    pass


@app.post('/finish')
def finish():
    pass




if __name__ == '__main__':
    app.run('127.0.0.1', 5000)