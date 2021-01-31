from flask import Flask, render_template, request, redirect, url_for, session
import models.database

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
        
        if (passwd != c_pass):
            return render_template('register.html.j2', diffPass=True)
        
        passwd = passwd.encode('utf8')
        hashPass, saltVal = models.database.saltHash(passwd)
        hashPass = hashPass.decode('utf-8')
        saltVal = saltVal.decode('utf-8')
        
        db = models.database.Connector()
        
        m = db.select_account(email)
        
        if (m is None or m.id != -1):
            return render_template('register.html.j2', emailExists=True)
        
        value = "'%s', '%s', '%s', '%s', '%s', '%s'" % (email, username, hashPass, saltVal, f_name, l_name)
        
        success = db.add_account(value)
        
        if (success):
            return render_template('index.html.j2', registerSuccess=True)
        else:
            return render_template('register.html.j2', registerFailed=True)


@app.route('/chat')
def chat():
    """
    GET the chat page
    """
    return render_template('chat.html.j2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Get the login page.
    """
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['password']
        
        db = models.database.Connector()
        m = db.select_account(email)
        
        if (m is None or m.id == -1):
            return render_template('login.html.j2', emailIncorrect=True)
        
        passwd = passwd.encode('utf-8')
        hashVal, slt = models.database.saltHash(passwd)
        
        hashVal = hashVal.decode('utf-8')
        
        if m.get_pass() == hashVal:
            return render_template('login.html.j2', passIncorrect=True)
        
        return redirect('blog')

    return render_template('login.html.j2')


@app.route('/blog')
def blog():
    """
    Get the blog page.
    """
    return render_template('blog.html.j2')


app.run()
