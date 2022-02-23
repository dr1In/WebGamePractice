from flask import Flask, jsonify, request

from Server_utils import Game, Lobby


app = Flask(__name__)


lobbies_list = dict()
users_ip_lobby = dict()
game_list = dict()

@app.post('/create_lobby')
def create_lobby():
    name_lobby = request.json['name']
    max_players = request.json['max']
    duration = request.json['month']
    username = request.json['user']
    ip = request.remote_addr
    users_ip_lobby[ip] = name_lobby

    if name_lobby not in lobbies_list:
        game_list[name_lobby] = Game(name_lobby, duration, max_players)
        lobbies_list[name_lobby] = Lobby(name_lobby, max_players, duration)
        lobbies_list[name_lobby].connect(username, ip)
        return jsonify(status = 'ok')
    else:
        return jsonify(status = 'name exception')


@app.get('/lobbies')
def lobbies():
    information = [{
        'lobby_name': _,
        'max': lobbies_list[_].get_emptiness(),
        'type': lobbies_list[_].get_dur()
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


@app.post('/connect')
def connect():
    username = request.json['user']
    ip_adr = request.remote_addr
    game_list[users_ip_lobby[ip_adr]].connect(username, ip_adr)
    return jsonify(answer = 'ok')


@app.get('/get_info')
def get_info():
    ip = request.remote_addr
    return jsonify(
        data= game_list[users_ip_lobby[ip]].collect_info(),
        user= game_list[users_ip_lobby[ip]].collect_player_info(ip)
    )


@app.post('/buy_raw')
def buy_raw():
    ip = request.remote_addr
    q = request.json['quantity']
    p = request.json['price']
    answer = game_list[users_ip_lobby[ip]].update_player_BR(ip, [int(q), int(p)])
    return jsonify(status = answer)


@app.post('/sell_planes')
def sell_planes():
    ip = request.remote_addr
    q = request.json['quantity']
    p = request.json['price']
    answer = game_list[users_ip_lobby[ip]].update_player_SP(ip, [int(q), int(p)])
    return jsonify(status = answer)


@app.post('/produce')
def produce():
    ip = request.remote_addr
    q = request.json['quantity_planes']
    answer = game_list[users_ip_lobby[ip]].produce_plane(ip, int(q))
    return jsonify(status = answer)


@app.post('/build')
def build():
    ip = request.remote_addr
    q = request.json['ask']
    answer = game_list[users_ip_lobby[ip]].build(ip, q)
    return jsonify(status = answer)


@app.post('/finish')
def finish():
    ip = request.remote_addr
    game_list[users_ip_lobby[ip]].change_player_status(ip)
    return jsonify(status = 'ok')


@app.get('/game_status')
def game_status():
    ip = request.remote_addr
    return jsonify(status = game_list[users_ip_lobby[ip]].get_game_status())


@app.get('/player_status')
def player_status():
    ip = request.remote_addr
    return jsonify(status = game_list[users_ip_lobby[ip]].player_status(ip))


if __name__ == '__main__':
    app.run('192.168.0.18', 5000)