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
    book_list = [
        {
            'name': "Crack The Code",
            'author': "Patrick C",
            'poster': "https://i.ibb.co/mSHhTXC/Crack-the-code.jpg"
        },
        {
            'name': "The Way of Nameless",
            'author': "Graham D",
            'poster': "https://i.ibb.co/cy5jmW6/The-way-of-nameless.jpg"
        },
        {
            'name': "Breaking Regulations",
            'author': "Victor S",
            'poster': "https://i.ibb.co/Kmwf6M8/Breaking-regulations.jpg"
        },
        {
            'name': "Broken Stars",
            'author': "Ken Liu",
            'poster': "https://i.ibb.co/sR6fxSR/Broken-stars.jpg"
        },
        {
            'name': "Lunar Storm",
            'author': "Terry Crosby",
            'poster': "https://i.ibb.co/sPs5JTS/Lunar-storm.jpg"
        },
        {
            'name': "The Martian",
            'author': "Andy Weir",
            'poster': "https://i.ibb.co/LvMLfVG/The-Martian.jpg"
        },
        {
            'name': "Another World",
            'author': "Samuel Best",
            'poster': "https://i.ibb.co/BPZH9Cw/Another-world.jpg"
        },
    ]
    return render_template('books.html', books=book_list)


demo.run(debug=True)
