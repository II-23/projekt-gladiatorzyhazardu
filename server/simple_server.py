from flask import Flask, request, jsonify

app = Flask(__name__)

players = []
tables = []

@app.route('/join', methods=['POST'])
def join_game():
    data = request.json
    player_name = data.get('name')
    players.append(player_name)
    return jsonify({'message': f'{player_name} joined the game'})

@app.route('/get_players', methods=['GET'])
def get_players():
    return jsonify({'players': players})

if __name__ == '__main__':
    app.run(debug=True)