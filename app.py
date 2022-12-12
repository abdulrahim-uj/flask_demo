from flask import Flask

flasksite = Flask(__name__)


@flasksite.route('/')
def home():
    return '<h1>Hello Flask</h1>'


@flasksite.route('/new-path/')
def new_path():
    return '<h2>This is new page</h2>'


@flasksite.route('/profile/<username>/<int:age>/')
def profile(username, age):
    return '<h1>This profile is for %s</h1>' % username + \
           '<h2>aged %d</h2>' % age


flasksite.run()
