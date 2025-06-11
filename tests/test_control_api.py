import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control_api.app import app


def test_register_and_commands():
    client = app.test_client()
    response = client.post('/register', json={'id': 'agent1', 'upload_url': 'http://localhost:5001/upload'})
    assert response.status_code == 201
    resp = client.post('/start/agent1')
    assert resp.status_code == 200
    resp = client.post('/stop/agent1')
    assert resp.status_code == 200
