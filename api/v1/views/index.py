#!/usr/bin/python3
"""The index folder package"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """Return the status of the page"""
    status = {
            'status': 'OK'
            }
    return jsonify(status)
