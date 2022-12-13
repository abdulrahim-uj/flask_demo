from flask import Flask, render_template

demo = Flask(__name__)


@demo.route('/')
def index():
    return render_template('index.html')


@demo.route('/profile/<username>')
def peofile(username):
    return render_template('profile.html', username=username, isActive=False)


@demo.route('/books/')
def book():
    book_list = ['book A', 'book B', 'book C', 'book D', 'book E']
    return render_template('books.html', books=book_list)


demo.run(debug=True)
