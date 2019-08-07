from flask import Flask, request, render_template, redirect, session, url_for, g
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField
from datetime import datetime

import random
import string
import pickledb

# export FLASK_APP=app.py
# flask run

def is_url(form, field):
    if not field.data.startswith('https://'):
        raise validators.ValidationError('A valid url is required')

class URLForm(FlaskForm):
    url = StringField('url', [is_url])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['PICKLE_DB'] = 'urls.db'

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


@app.route('/', methods=['GET', 'POST'],  defaults={'url_id': None})
@app.route('/<url_id>', methods=['GET', 'POST'])
def create_url(url_id):
    
    db = get_db()
    
    if url_id:
        return redirect(db.get(url_id))

    form = URLForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        url = form.url.data
        key = ''.join([random.choice(string.ascii_lowercase) for _ in range(3)] + [random.choice(string.digits) for _ in range(3)])
        db.set(key, url)
        db.dump()
        session['url'] =  url
        session['short_url'] = f'{request.base_url}{key}'
        form.url.data = None
        return redirect(url_for('create_url'))

    return render_template('index.html', form=form, url=session.get('url', None))

