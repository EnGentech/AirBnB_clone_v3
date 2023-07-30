#!/usr/bin/python3

from models import storage
from models.state import State
from flask import jsonify, Flask
import json


states = storage.all(State).values()
new_dict = []
for state in states:
    new_dict.append(state.to_dict())


a = '189b619-8a07-4f66-9da6-6acb0c8bce96'
for i in new_dict:
    if i['id'] == a:
        print(i)
        break
    else:
        print("None")
