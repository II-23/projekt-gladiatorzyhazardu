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

# players database
PLAYER_DB = {}

# tables database
TABLE_DB = {}

@app.route('/create_player', methods=['POST'])
def create_player():
    data = request.json

    nickname = data['nickname']
    player_id = str(uuid.uuid4())

    PLAYER_DB[player_id] = Player(player_id, nickname)

    print(f'Created new player with ID: {player_id} with nickname: {nickname}')

    return jsonify({'message:': f'New player is created with id={player_id} nickname={nickname}','player_id': player_id})

@app.route('/create_table', methods=['POST'])
def create_table():
    admin_id = data.get('player_id')

    if admin_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{admin_id}" does not exist'})

    table_id = str(uuid.uuid4())

    tables[table_id] = {
        'table_id': table_id,
        'admin_id': admin_id,
        'table': Table()
    }

    print(f'Created new table with ID: {table_id} by {admin_id}')

    return jsonify({'message': f'Table {table_id} is created','table_id': table_id})

@app.route('/join_table', methods=['POST'])
def join_table():
    data = request.json

    player_id = data.get('player_id')
    if player_id not in players:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in tables:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})

    player = players[player_id]
    tables[table_id].addPlayer(player)

    print(f'Player {player_id} joined table {table_id}')

    return jsonify({'message': f'{player_id} joined the table {table_id}'})


@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json

    admin_id = data.get('player_id')
    if admin_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{admin_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    if TABLE_DB[table_id]['admin_id'] != admin_id:
        return jsonify({'message': f'ERROR: You({admin_id}) are not the admin of table {table_id}'})
    
    TABLE_DB[table]['table'].startGame()

    return jsonify({'message': f'Table {table_id} started successfully'})

@app.route('/get_table', methods=['GET'])
def get_table():
    data = request.json
    
    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    table = TABLE_DB[table_id]

    return jsonify()

@app.route('/make_bid', methods=['POST'])
def make_bid():
    data = request.json

    player_id = data.get('player_id')
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    bid = data.get('bid')

    TABLE_DB[table_id]['table'].play(player_id, bid)

    print(f'Bid {bid} is player by {player_id} on {table_id}')

    return jsonify({'message': f'Successfuly bided on {table_id} by {player_id}'})


@app.route('/get_all_players', methods=['GET'])
def get_all_players():
    return jsonify({'players': list(PLAYER_DB.keys())})

@app.route('/get_all_tables', methods=['GET'])
def get_all_tables():
    return jsonify({'tables': list(TABLE_DB.keys())})

if __name__ == '__main__':
    print("HOST: ", config.server['host'])
    print("PORT: ", config.server['port'])
    app.run(host=config.server['host'], port=config.server['port'], debug=True)