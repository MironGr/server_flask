import json
import pickle
from flask import Response


def delete_users():
    """Delete users"""
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)
    data_new.clear()
    return Response('{"status": "clear"}', status=200)


def get_users():
    """Get info about user"""
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)
    js = json.dumps(data_new)
    pickle_in.close()
    return Response(js, status=200, mimetype='application/json')

# create_users() == user.create_user()