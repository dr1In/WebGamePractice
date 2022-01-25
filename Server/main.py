from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/lobbys')
def get_lobbys():
    return




if __name__ == '__main__':
    app.run()