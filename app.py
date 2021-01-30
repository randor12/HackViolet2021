from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route('/hello')
def hello():
    """
    Get Request for "hello"
    :return: returns 'Hello World'
    """
    return 'Hello, World!'


@app.route('/')
def index():
    """
    Get request for the index page.
    :return: returns the rendered HTML page
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Get request for the about page.
    :return: returns the rendered HTML page
    """
    return render_template('about.html')


app.run()
