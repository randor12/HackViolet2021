from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get request for the index page.
    :return: returns the rendered HTML page
    """
    if (request.method == 'GET'):
        return render_template('index.html.j2')
    elif request.method == 'POST':
        location = request.form['location']
        if location is not None:
            print('Location', location)
        else:
            print("Could not get location")
        return redirect(url_for('register'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    Get request for the about page.
    :return: returns the rendered HTML page
    """
    if (request.method == 'GET'):
        return render_template('register.html.j2')
    else:
        # TODO: For ROI
        email = request.form['email']
        username = request.form['username']
        passwd = request.form['password']
        c_pass = request.form['confirmPassword']
        f_name = request.form['fName']
        l_name = request.form['lName']
        return render_template('index.html.j2')


@app.route('/chat')
def chat():
    """
    GET the chat page
    """
    return render_template('chat.html.j2')


@app.route('/login')
def login():
    """
    Get the login page.
    """
    return render_template('login.html.j2')


@app.route('/blog')
def blog():
    """
    Get the blog page.
    """
    return render_template('blog.html.j2')


app.run()
