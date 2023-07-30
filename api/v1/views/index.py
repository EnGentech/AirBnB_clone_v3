#!/usr/bin/python3
"""The index folder package"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City


@app_views.route('/status')
def status():
    """Return the status of the page"""
    status = {
            'status': 'OK'
            }
    return jsonify(status)

@app_views.route('/api/v1/stats')
def count():
    """Return the number of each objects in database"""
    objects = {
            'amenities': Amenity,
            'cities': City,
            'places': Place,
            'reviews': Review,
            'states': States,
            'users': User
            }   
    my_dict = {}
    for key, value in objects.items():
        new_dict = {
                key: storage.count(value)
                }
        my_dict.update(new_dict)
    return jsonify(my_dict)
