import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from logic.table import Table
from logic.player import Player
import config

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

players = {}
tables = {}

@app.route('/create_player', methods=['POST'])
def create_player():
    data = request.json

    player_id = str(uuid.uuid4())

    players[player_id] = Player(0, player_id)

    print("NEW PLAYER ID: ", player_id)
    print("PLAYERS: ", players)

    return jsonify(
        {
            'message:': f'New player is created with id={player_id}',
            'player_id': player_id
        }
    )

@app.route('/create_table', methods=['POST'])
def create_table():
    data = request.json

    admin_id = data.get('player_id')

    if admin_id not in players:
        return jsonify(
            {
                'message': f'Player "{admin_id}" does not exist'
            }
        )

    table_id = str(uuid.uuid4())

    tables[table_id] = {
        'table_id': table_id,
        'admin_id': admin_id,
        'table': Table()
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
    if player_id not in players:
        return jsonify(
            {
                'message': f'Player "{player_id}" does not exist'
            }
        )

    table_id = data.get('table_id')
    if table_id not in tables:
        return jsonify(
            {
                'message': f'Table "{table_id}" does not exist'
            }
        )

    player = players[player_id]

    tables[table_id].addPlayer(player)

    return jsonify(
        {
            'message': f'{player_id} joined the table {table_id}'
        }
    )

@app.route('/get_players', methods=['GET'])
def get_players():
    return jsonify({'players': list(players.keys())})

@app.route('/get_tables', methods=['GET'])
def get_tables():
    return jsonify({'tables': list(tables.keys())})

if __name__ == '__main__':
    print("HOST: ", config.server['host'])
    print("PORT: ", config.server['port'])
    app.run(host=config.server['host'], port=config.server['port'], debug=True)