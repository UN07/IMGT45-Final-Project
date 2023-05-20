from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
import database as db
import authentication
import logging

app = Flask(__name__)

# Set the secret key to some random bytes.
# Keep this really secret!
app.secret_key = b's@g@d@c0ff33!'


logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)



@app.route('/')
def index():
    return render_template('homepage.html', page="homepage")

@app.route('/profile')
def profile():
    return render_template('profile.html', page="profile")

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="aboutus")

@app.route('/feed')
def feed():
    return render_template('feed.html', page="feed")

@app.route('/discover')
def discover():
    return render_template('discover.html', page="discover")

@app.route('/discover2')
def discover2():
    return render_template('discover2.html', page="discover2")

@app.route('/chats')
def chats():
    return render_template('chats.html', page="chats")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    app.logger.info('%s', is_successful)
    if(is_successful):
        session["user"] = user
        return redirect('/feed')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect('/')

