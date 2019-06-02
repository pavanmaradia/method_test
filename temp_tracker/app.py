"""
Temperature Tracker application

__author__ = 'Pavan Maradia'
__version__ = 'v1.0'

"""

from os import environ

from flask import Flask, jsonify, request
from flask_cors import CORS

from temp_tracker.temperature.api import TempTracker
from temp_tracker.utility import jsonify_request

# Remove following lines while deploy in production
environ.update({
    'db_username': 'root',
    'db_password': 'root',
    'db_host': 'localhost',
    'db_name': 'temp_tracker',
    'db_port': '5432'
})

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/temperature', methods=['POST'])
def temperature():
    """
    Temperature API for POST, GET, PUT, DELETE
    :return:
    """
    response = {}

    if request.method == 'POST':
        payload = jsonify_request(request)
        response = TempTracker().controller(**{
            'method': 'insert',
            'payload': payload,
            'response': 'flask_resp'
        })

    return jsonify(**response)


@app.route('/api/v1/temperature/max', methods=['GET'])
def temperature_get_max():
    """
    Temperature to get maximum temperature from database
    :return:
    """
    response = {}

    if request.method == 'GET':
        response = TempTracker().controller(**{
            'method': 'get_max',
            'payload': {},
            'response': 'flask_resp'
        })

    return jsonify(**response)


@app.route('/api/v1/temperature/min', methods=['GET'])
def temperature_get_min():
    """
    Temperature to get minimum temperature from database
    :return:
    """
    response = {}

    if request.method == 'GET':
        response = TempTracker().controller(**{
            'method': 'get_min',
            'payload': {},
            'response': 'flask_resp'
        })

    return jsonify(**response)


@app.route('/api/v1/temperature/mean', methods=['GET'])
def temperature_get_mean():
    """
    Temperature to get minimum temperature from database
    :return:
    """
    response = {}

    if request.method == 'GET':
        response = TempTracker().controller(**{
            'method': 'get_mean',
            'payload': {},
            'response': 'flask_resp'
        })

    return jsonify(**response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
