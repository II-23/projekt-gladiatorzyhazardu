import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import requests
from logic import game_start

import config
import asyncio

base_url = f"http://{config.server['host']}:{config.server['port']}"

def join_table(player_id, table_id):
    response = requests.post(f'{base_url}/join_table', json={'player_id': player_id, 'table_id': table_id})
    print(response.json())

def get_all_players():
    response = requests.get(f'{base_url}/get_all_players', json={})
    print(response.json())

    data = response.json()
    return data['players']

def get_all_tables():
    response = requests.get(f'{base_url}/get_all_tables', json={})
    print(response.json())
    
    data = response.json()
    return data['tables']

def register():
    response = requests.post(f'{base_url}/create_player', json={})
    print(response.json())
    
    data = response.json()
    return data['player_id']

def create_table(player_id):
    response = requests.post(f'{base_url}/create_table', json={'player_id': player_id})
    print(response.json())

    data = response.json()
    return data['table_id']

def start_game(player_id, table_id):
    response = requests.post(f'{base_url}/start_game', json={'player_id': player_id, 'table_id': table_id})
    print(response.json())

def get_table(table_id):
    response = requests.get(f'{base_url}/get_table', json={'table_id': table_id})
    print(response.json())

def make_bid(player_id, table_id, bid):
    response = requests.post(f'{base_url}/make_bid', json={'player_id': player_id, 'table_id': table_id, 'bid': bid})
    print(response.json())

def register(nickname):
    response = requests.post(f'{base_url}/create_player', json={'nickname': nickname})
    print(response.json())
    
    data = response.json()
    return data['player_id']

# asyncronicaly ping the server in the background to inform that player is alive
async def ping_server(player_id):
    while True:
        response = requests.post(f'{base_url}/ping', json={'player_id': player_id})
        print('Ping')
        await asyncio.sleep(3)

async def main():
    nickname = input("Nickname:")
    my_id = register(nickname)

    print(f'My id: {my_id}')

    await asyncio.gather(ping_server(my_id))

    while True:
        command = input('>').split()

        if "create_table" in command[0]:
            create_table(my_id)
        elif "join_table" in command[0]:
            join_table(command[1], command[2])
        elif "start_game" in command[0]:
            start_game(command[1], command[2])
        elif "get_table" in command[0]:
            get_table(command[1])
        elif "make_bid" in command[0]:
            make_bid(command[1], command[2], command[3])
        elif "get_all_players" in command[0]:
            print(get_all_players())
        elif "get_all_tables" in command[0]:
            print(get_all_tables())
        else:
            print("No command matching")

if __name__ == '__main__':
    asyncio.run(main())