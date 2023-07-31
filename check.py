#!/usr/bin/python3

from models import storage
from models.state import State
from flask import jsonify, Flask
from sys import argv
import json


states = storage.all(State).values()
new_dict = []
for state in states:
    new_dict.append(state.to_dict())

value = 0
a = argv[1]
for i in new_dict:
    if i['id'] == a:
        print(i)
        value = 1
        break
        
if value == 0:
    print("None")
