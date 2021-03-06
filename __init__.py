from flask import Flask, render_template, request, redirect, url_for, session
from HackViolet2021.models.SentimentAnalysis.classifier import SentimentClassifier
import os
import HackViolet2021.models.database


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


def predict_phrase(txt: str) -> str:
    """
    :param txt: text to be predicted as positive or negative
    :return: returns Positive if predicted as positive, else Negative
    """
    model = SentimentClassifier()
    return model.predict(txt)


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

        value = "'%s', '%s', '%s', '%s', '%s', '%s'" % (
            email, username, hashPass, saltVal, f_name, l_name)

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

        session['user-value'] = m.get_email()
        return redirect('blog')

    return render_template('login.html.j2')


@app.route('/logout')
def logout():
    session.pop('user-value', None)
    return render_template('index.html.j2')


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    """
    Get the blog page.
    """

    db = models.database.Connector()
    feedMsgs = db.get_feed_msgs()
    userInfo = db.select_account(session['user-value'])

    if (request.method == 'GET'):
        if ('user-value' in session.keys()):
            return render_template('blog.html.j2', msgList=feedMsgs, accInfo=userInfo)
        else:
            return render_template('index.html.j2')
    else:
        title = request.form['title']
        message = request.form['message']
        # return 'You entered: {}'.format(message)

        if (message is None or title is None):
            return render_template('blog.html.j2')

        title_sentiment = predict_phrase(title)
        sentiment = predict_phrase(message)

        if (title_sentiment == sentiment and sentiment == 'Positive'):
            # add message to DB and post to Blog
            userID = userInfo.get_id()

            values = [userID, title, message, 1, -1]
            success = db.add_msg(*values)

        else:
            # Send Notificatin -> Message must be positive
            return render_template('blog.html.j2', msgList=feedMsgs, negativeMessageSent=True, accInfo=userInfo)

        ## success = db.add_msg(userID, message, 1, -1)

        if (success):
            feedMsgs = db.get_feed_msgs()
            return render_template('blog.html.j2', msgList=feedMsgs, accInfo=userInfo)
        else:
            return render_template('blog.html.j2', msgList=feedMsgs, accInfo=userInfo)


if __name__ == '__main__':
    app.run()
