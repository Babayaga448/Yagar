import os
from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

# Store connected players with timestamp for cleanup
players = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/join', methods=['POST'])
def join_game():
    try:
        data = request.json
        player_id = data.get('id')
        players[player_id] = {
            'x': data['x'],
            'y': data['y'],
            'radius': data['radius'],
            'color': data['color'],
            'score': 0,
            'last_update': datetime.now().timestamp()
        }
        return jsonify({'success': True, 'players': players})
    except Exception as e:
        logger.error(f"Error in join_game: {str(e)}")
        return jsonify({'error': 'Failed to join game'}), 500

@app.route('/api/update', methods=['POST'])
def update_player():
    try:
        data = request.json
        player_id = data.get('id')
        if player_id in players:
            players[player_id].update({
                'x': data['x'],
                'y': data['y'],
                'radius': data['radius'],
                'score': data['score'],
                'last_update': datetime.now().timestamp()
            })

            # Clean up inactive players (more than 10 seconds without update)
            current_time = datetime.now().timestamp()
            inactive_players = [pid for pid, p in players.items() 
                              if current_time - p['last_update'] > 10]
            for pid in inactive_players:
                del players[pid]

        return jsonify({'players': players})
    except Exception as e:
        logger.error(f"Error in update_player: {str(e)}")
        return jsonify({'error': 'Failed to update player'}), 500

if __name__ == '__main__':
    # Always serve the app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)