import json
import pickle
from flask import Response

data = {}


def create_user(user=None):
    """Actions Create==Update"""
    pickle_in = open('data.pickle', 'r+b')
    data_new = pickle.load(pickle_in)
    for key in data_new.keys():
        if key == user:
            return Response('{"status": "create"}', status=200)
        elif key != user:
            data_new[user] = data[{'name': 'Ivan', 'age': '25'}]
            pickle.dump(data_new, pickle_in)
    pickle_in.close()
    return Response('{"status": "ok"}', status=200)


def delete_user(user=None):
    """Delete user"""
    pickle_in = open('data.pickle', 'wb')
    data_new = pickle.load(pickle_in)
    for key in data_new.keys():
        if key == user:
            del data_new[user]
            return Response('{"status": "remote"}', status=200)
        elif key != user:
            return Response('{"status": "none"}', status=200)


def get_user(user=None):
    """Get info about user"""
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)
    for key in data_new.keys():
        if key == user:
            js = json.dumps(data_new[key])
            return Response(js, status=200)
        elif key != user:
            return Response('{"status": "none"}', status=200)
    pickle_in.close()
