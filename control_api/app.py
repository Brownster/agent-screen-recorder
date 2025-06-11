from flask import Flask, request, jsonify

app = Flask(__name__)

agents = {}

@app.route('/register', methods=['POST'])
def register_agent():
    data = request.get_json()
    agent_id = data['id']
    agents[agent_id] = data['upload_url']
    return jsonify({'status': 'registered'}), 201

@app.route('/start/<agent_id>', methods=['POST'])
def start_recording(agent_id):
    # In a real system we would send a message to the agent
    if agent_id not in agents:
        return jsonify({'error': 'unknown agent'}), 404
    return jsonify({'status': 'start command sent'})

@app.route('/stop/<agent_id>', methods=['POST'])
def stop_recording(agent_id):
    if agent_id not in agents:
        return jsonify({'error': 'unknown agent'}), 404
    return jsonify({'status': 'stop command sent'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
