#!/usr/bin/python3
"""
Create flask web application
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


host_use = getenv('HBNB_API_HOST')
port_use = getenv('HBNB_API_PORT')

if host_use:
    hst = host_use
else:
    hst = '0.0.0.0'

if port_use:
    pt = port_use
else:
    pt = 5000

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def storage_close(self):
    """a teardown context to close the session"""
    storage.close()


@app.route('/api/v1/nop')
def err_404():
    """A function to return error 404"""
    err = {'error': 'Not found'}
    return jsonify(err)


if __name__ == "__main__":
    app.run(host=hst, port=pt, threaded=True)
