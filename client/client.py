import requests
from ../ import game_start

base_url = 'http://165.232.32.194:2137'

def join_game(player_name):
    response = requests.post(f'{base_url}/join', json={'name': player_name})
    print(response.json())

def get_players():
    response = requests.get(f'{base_url}/get_players')
    print(response.json())

if __name__ == '__main__':
    player_name = input('Enter your name:')
    join_game(player_name)
    get_players()