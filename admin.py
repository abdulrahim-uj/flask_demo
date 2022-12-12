from flask import Flask, render_template

demo = Flask(__name__)


@demo.route('/')
def index():
    return render_template('index.html')


demo.run(debug=True)
