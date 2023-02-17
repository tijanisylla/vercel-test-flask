from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET'])
def test_get():
    return jsonify({'message': 'Hello World!'})


@app.route('/test2', methods=['GET'])
def test_get_2():
    return jsonify({'message': 'Hello World! 2'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
