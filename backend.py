from flask import Flask, request, jsonify
from analyse import analyze_message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message received'}), 400

    response = analyze_message(user_message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
