from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)
    return jsonify({'status': 'stored', 'path': filepath})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
