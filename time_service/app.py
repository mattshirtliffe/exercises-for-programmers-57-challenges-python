from datetime import datetime

# export FLASK_APP=app.py
# flask run
    
from flask import Flask
app = Flask(__name__)


def get_now():
    return datetime.utcnow()

@app.route('/')
def get_time():
    return {'current_time':get_now()}