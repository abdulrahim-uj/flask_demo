from flask import Flask, render_template

demo = Flask(__name__)


@demo.route('/')
def index():
    return render_template('index.html')


@demo.route('/profile/<username>')
def peofile(username):
    return render_template('profile.html', username=username, isActive=True)


demo.run(debug=True)
