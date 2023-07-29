#!/usr/bin/python3
"""
Create flask web application
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask('__name__')
app.register_blueprint(app_views)

@app.teardown_appcontext
def storage_close(self):
    return storage.close()

if __name__ == "__main__":
    app.run(debug=True)
