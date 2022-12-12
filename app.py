from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello Flask</h1>'


@app.route('/new-path/')
def new_path():
    return '<h2>This is new page</h2>'


app.run()
