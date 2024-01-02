import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import requests
from logic import game_start

import config

base_url = f"http://{config.server['host']}:{config.server['port']}"

def join_table(player_id):
    response = requests.post(f'{base_url}/join', json={'name': player_name})
    print(response.json())

def get_players():
    response = requests.get(f'{base_url}/get_players', json={})
    # print(response.json())

    data = response.json()
    return data['players']

def get_tables():
    response = requests.get(f'{base_url}/get_tables', json={})
    # print(response.json())
    
    data = response.json()
    return data['tables']

def register():
    response = requests.post(f'{base_url}/create_player', json={})
    # print(response.json())
    
    data = response.json()
    return data['player_id']

def create_table(my_id):
    response = requests.post(f'{base_url}/create_table', json={'player_id': my_id})

    data = response.json()
    return data['table_id']

if __name__ == '__main__':
    my_id = register()

    print("REGISTER SUCCESSFULY")

    print("players: ", get_players())

    create_table(my_id)

    print("tables: ", get_tables())