import sys
sys.path.append('..') # used for importing files from parent folder

from logic import Table
import config

from flask import Flask, request, jsonify

app = Flask(__name__)

players = {}
tables = {}

@app.route('/create_player', method=['POST'])
    data = request.json

    player_id = str(uuid.uuid4())

    players[player_id] = Player(0, player_id)

    return jsonify(
        {
            'message:' f'New player is created with id={player_id}',
            'player_id': player_id
        }
    )

@app.route('/create_table', method=['POST'])
def create_table():
    data = request.json

    admin_id = data.get('player_id')

    if admin_id is not in players:
        return jsonify(
            {
                'message': f'Player "{admin_id}" does not exist'
            }
        )

    table_id = str(uuid.uuid4())

    tables[table_id] = {
        'table_id': table_id,
        'admin_id': admin_id,
        'table': Table(1)
    }

    return jsonify(
        {
            'message': f'Table {table_id} is created',
            'table_id': table_id
        }
    )

@app.route('/join_table', methods=['POST'])
def join_table():
    data = request.json
    player_id = data.get('player_id')
    table_id = data.get('table_id')

    tables[table_id].addPlayer(player_id)

    players.append(player_name)
    return jsonify(
        {
            'message': f'{player_name} joined the game'
        }
    )

@app.route('/get_players', methods=['GET'])
def get_players():
    return jsonify({'players': players})

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], debug=True)