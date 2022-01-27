from flask import Flask, jsonify, request

from Server_utils import Game, Player

app = Flask(__name__)


game = Game()


@app.post('/connect')
def connect():
    name = request.json['name']
    text = game.connection(Player(name))
    return jsonify(status=text)



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
    app.run()