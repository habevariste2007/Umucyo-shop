from flask import Flask, request, jsonify, render_template
import json, os

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'mtbs_data.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    return jsonify({'message': 'Data saved successfully'})

@app.route('/load', methods=['GET'])
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({})

# Use PORT from environment when deployed
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
