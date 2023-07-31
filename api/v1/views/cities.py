#!/usr/bin/python3
"""Retrieving State objects"""

from models.city import City
from flask import request
from api.v1.views import app_views

my_dict = City().to_dict()


@app_views.route('/cities', methods=["GET", "POST"], strict_slashes=False)
def get_post():
    if request.method == 'GET':
        return jsonify(dic)
    elif request.method == 'POST':
        name = request.get_json()
        if name['name'] is None:
            return 'Missing name', 400
        try:
            value = name['name']
            new_dict = {
                '__class__': City.__name__,
                'created_at': State().created_at,
                'name': value,
                'id': State().id,
                'updated_at': State().updated_at
            }
            return new_dict, 201

        except Exception as e:
            return jsonify("Not a JSON"), 400
