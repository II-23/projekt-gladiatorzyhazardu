import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import requests
from logic import game_start

base_url = f'http://{config.host}:{config.port}'

def join_table(player_id):
    response = requests.post(f'{base_url}/join', json={'name': player_name})
    print(response.json())

def get_players():
    response = requests.get(f'{base_url}/get_players')
    print(response.json())

    return response['players']

def get_tables():
    response = requests.get(f'{base_url}/get_tables')
    print(response.json())
    
    data = response.json()
    return data['tables']

def register():
    response = requests.post(f'{base_url}/create_player')
    print(response.json())
    
    data = response.json()
    return data['player_id']

if __name__ == '__main__':
    my_id = register()

    print(get_players())