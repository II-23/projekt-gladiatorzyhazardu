import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from logic.table import Table
from logic.player import Player
import config
import time

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# players database
PLAYER_DB = {} # dict[str, Player]

# tables database
TABLE_DB = {} # dict[str, dict[str, Table/str]]

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
    data = request.json

    admin_id = data.get('player_id')
    if admin_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{admin_id}" does not exist'})

    table_id = str(uuid.uuid4())

    TABLE_DB[table_id] = {
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
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})

    if len(TABLE_DB[table_id]['table'].players) >= 23:
        return jsonify({'message': f'ERROR: Game on Table "{table_id}" has too many players (23)'})

    PLAYER_DB[player_id].table_id = table_id

    player = PLAYER_DB[player_id]
    TABLE_DB[table_id]['table'].addPlayer(player)

    print(f'Player {player_id} joined table {table_id}')

    return jsonify({'message': f'{player_id} joined the table {table_id}'})

@app.route('/leave_table', methods=['POST'])
def leave_table():
    data = request.json

    player_id = data.get('player_id')
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    table_id = PLAYER_DB[player_id].table_id
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist or you havent join any.'})
    
    if TABLE_DB[table_id]['table'].removePlayer(player_id) == False:
        return jsonify({'message': f'ERROR: Failed to leave the table "{table_id}". removePlayer() failed.'})

    return jsonify({'message': f'{player_id} left the table {table_id}'})

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
    
    TABLE_DB[table_id]['table'].startGame()

    return jsonify({'message': f'Table {table_id} started successfully'})

@app.route('/get_table', methods=['GET'])
def get_table():
    data = request.json
    
    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    table = TABLE_DB[table_id]['table']

    players_in_table = [(p.nickname, p.id,p.active) for p in table.players]
    cards_of_players = [list(str(c) for c in p.cards_on_hand) for p in table.players]

    tmp_players=table.players
    admin_index=(-1,TABLE_DB[table_id]['admin_id'])
    for i in range(len(tmp_players)):
        if tmp_players[i].id==TABLE_DB[table_id]['admin_id']: 
            admin_index=(i,TABLE_DB[table_id]['admin_id'])
            break

    # print("cards:", cards_of_players)
    # print("players:", players_in_table)

    return jsonify(
                {
                    'players': players_in_table,
                    'admin': admin_index,
                    'admin_id': TABLE_DB[table_id]['admin_id'],
                    'cards': cards_of_players,
                    'start_player': table.first_player,
                    'bids': table.bid_history,
                    'current_index': table.current_index,
                    'game_started': table.started,
                    'looser' :table.looser,
                    'nickbid' :table.nickbid_history
                }
            )

@app.route('/make_bid', methods=['POST'])
def make_bid():
    data = request.json

    player_id = data.get('player_id')
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    if TABLE_DB[table_id]['table'].getCurrentPlayer() != player_id:
        return jsonify({'message': f'ERROR: It is not turn of Player "{player_id}" on Table "{table_id}"'})

    bid = data.get('bid')
    if TABLE_DB[table_id]['table'].play(player_id, bid) == False:
        return jsonify({'message': f'ERROR: Failed to make a bid'})

    print(f'Bid {bid} is played by {player_id} on {table_id}')

    return jsonify({'message': f'Successfuly bid on {table_id} by {player_id}'})

@app.route('/get_all_players', methods=['GET'])
def get_all_players():
    return jsonify({'players': list(PLAYER_DB.keys())})

@app.route('/get_all_tables', methods=['GET'])
def get_all_tables():
    return jsonify({'tables': list(TABLE_DB.keys())})

# simple mechanism that is used to determine 
# wherether there is connection with the player
@app.route('/ping', methods=['POST'])
def ping():
    data = request.json

    print(PLAYER_DB)

    for player_id, player in PLAYER_DB.copy().items():
        if time.time() - player.last_ping > 5:
            print("TIMEOUT: ", player_id, "FROM", player.table_id)
            if player.table_id != -1:
                TABLE_DB[player.table_id]['table'].removePlayer(player_id)
                TABLE_DB[player.table_id]['looser'] = None
                # table is now empty, remove it
                if len(TABLE_DB[player.table_id]['table'].players) == 0:
                    TABLE_DB.pop(player.table_id)

            PLAYER_DB.pop(player_id)
    
    player_id = data.get('player_id')
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist (probably timeout)'})

    print("PING BY: ", player_id)
    PLAYER_DB[player_id].last_ping = time.time()

    return jsonify({'message': 'Ping successfuly'})

@app.route('/end_game', methods=['POST'])
def end_game():
    data = request.json

    admin_id = data.get('player_id')
    if admin_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{admin_id}" does not exist'})

    table_id = data.get('table_id')
    if table_id not in TABLE_DB:
        return jsonify({'message': f'ERROR: Table "{table_id}" does not exist'})
    
    if TABLE_DB[table_id]['admin_id'] != admin_id:
        return jsonify({'message': f'ERROR: You({admin_id}) are not the admin of table {table_id}'})
    
    TABLE_DB[table_id]['table'].endGame()

    return jsonify({'message': f'Table {table_id} ended successfully'})

@app.route('/id_to_nick', methods=['POST'])
def id_to_nick():
    data = request.json

    player_id = data.get('player_id')
    if player_id not in PLAYER_DB:
        return jsonify({'message': f'ERROR: Player "{player_id}" does not exist'})

    player = PLAYER_DB[player_id]

    return jsonify({'nickname': player.nickname})


if __name__ == '__main__':
    print("HOST: ", config.server['host'])
    print("PORT: ", config.server['port'])
    app.run(host=config.server['host'], port=config.server['port'], debug=True)
