"""
Test file to run both program
"""

import os

from temp_tracker.temperature.api import TempTracker

os.environ.update({
    'db_username': 'root',
    'db_password': 'root',
    'db_host': 'localhost',
    'db_name': 'temp_tracker',
    'db_port': '5432'
})


def flatten_list_test():
    from flatten_list import ListFlatten
    x = [1, 2, [3, [4]], 5]
    print(ListFlatten().controller(x))
    x = [12, 21, 3, [4,[5], [6, [7], 8, [9, [10, 11]]]]]
    print(ListFlatten().controller(x))


def insert_data():
    temp_range = [i for i in range(0, 110)]
    from random import choice

    for i in range(1):
        payload = {
            'method': 'insert',
            'payload': {
                'temperature': choice(temp_range),
                'city': 'Pune'
            }
        }
        resp = TempTracker().controller(**payload)
        print(resp)


def get_max():
    payload = {
        'method': 'get_max',
        'response': 'flask_resp'
    }
    resp = TempTracker().controller(**payload)
    print(resp)


def get_min():
    payload = {
        'method': 'get_min'
    }
    resp = TempTracker().controller(**payload)
    print(resp)


def get_mean():
    payload = {
        'method': 'get_mean'
    }
    resp = TempTracker().controller(**payload)
    print(resp)


# flask Rest APIs

from requests import get, post


def get_max_flask():
    resp = get('http://localhost:5000/api/v1/temperature/max')
    print(resp.json())


def get_min_flask():
    resp = get('http://localhost:5000/api/v1/temperature/min')
    print(resp.json())


def get_mean_flask():
    resp = get('http://localhost:5000/api/v1/temperature/mean')
    print(resp.json())


def insert_flask():
    resp = post(
        url='http://localhost:5000/api/v1/temperature',
        data={'temperature': 45, 'city': 'Pune'}
    )
    print(resp.json())


flatten_list_test()
