import sys
sys.path.append('../logic') # used for importing files from parent folder

from logic import Table

from flask import Flask, request, jsonify


app = Flask(__name__)

players = {}
tables = {}

host = '165.232.32.194'
port = 2137

@app.route('/create_table', method=['POST'])
def create_table():
    data = request.json

    admin_id = data.get('admin_id')

    tables.add(
        {
            'admin_id': admin_id,
            'table': Table(1)
        }
    )

@app.route('/join', methods=['POST'])
def join_table():
    data = request.json
    player_name = data.get('name')
    players.append(player_name)
    return jsonify({'message': f'{player_name} joined the game'})

@app.route('/get_players', methods=['GET'])
def get_players():
    return jsonify({'players': players})

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)