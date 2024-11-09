import uuid
from logging.config import dictConfig

from flask import Flask, render_template, flash, url_for, redirect, request

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] - %(message)s',
        }
    },
    'handlers': {
        'stream': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': 'authorization_stub.log',
        },
    },
    'loggers': {
        'root': {
            'level': 'ERROR',
            'handlers': ['stream', 'file']
        },
        'waitress': {
            'level': 'INFO',
            'handlers': ['stream'],
            'propagate': False
        },
    }
})

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex


@app.route("/")
def base():
    return redirect(url_for('login_get'))


@app.get('/login')
def login_get():
    return render_template('login.html')


@app.post('/login')
def login_post():
    flash("Invalid username or password.", "error")
    app.logger.error('Detected an attempt to enter login and password [{0}] {1} {2}'.format(
        request.remote_addr, request.form['username'], request.form['password']
    ))

    return redirect(url_for('login_get'))
