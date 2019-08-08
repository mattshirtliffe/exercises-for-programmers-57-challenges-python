from flask import Flask, request, render_template, redirect, session, url_for, g
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField, TextAreaField
from datetime import datetime

import random
import string
import pickledb

# export FLASK_APP=app.py
# flask run


class URLForm(FlaskForm):
    text = TextAreaField('text')
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['PICKLE_DB'] = 'text.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = pickledb.load(app.config['PICKLE_DB'], False, sig=False)
        g.db = db
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.dump()
        # db.close()

@app.route('/', methods=['GET', 'POST'],  defaults={'text_id': None})
@app.route('/<text_id>', methods=['GET', 'POST'])
def create_text(text_id):
    form = URLForm()
    db = get_db()

    if request.method == 'POST' and form.validate_on_submit():
        text = form.text.data
       
        if text_id:
            key = text_id
            session['url'] = f'{request.base_url}'
        else:
            key = ''.join([random.choice(string.ascii_lowercase) for _ in range(3)] + [random.choice(string.digits) for _ in range(3)])
            session['url'] = f'{request.base_url}{key}'

        db.set(key, text)
        db.dump()

        form.text.data = None
        return redirect(url_for('create_text'))
    else:
        if text_id:
            form.text.data = db.get(text_id)
            text = db.get(text_id)
        else:
            text = None

    return render_template('index.html', form=form, url=session.get('url', None), text_id=text_id, text=text)

