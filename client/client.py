import sys
sys.path.append('..') 

import requests
from logic import game_start

base_url = f'http://{config.host}:{config.port}'

def join_game(player_name):
    response = requests.post(f'{base_url}/join', json={'name': player_name})
    print(response.json())

def get_players():
    response = requests.get(f'{base_url}/get_players')
    print(response.json())

if __name__ == '__main__':
    try:
        with open('../config.json', 'r') as config_file:
            config = json.load(config_file)
        
        host = config.host
        port = config.port
    except FileNotFoundError:
        print(f"Plik config.json nie istnieje")

if __name__ == '__main__':
    player_name = input('Enter your name:')
    join_game(player_name)
    get_players()