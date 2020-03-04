from flask import Flask, render_template, request, session, make_response, redirect, url_for
from static.database.database import Database
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
# app.secret_key = ''

dbmain = Database()

EMAIL_ADDRESS = 'graphical58@gmail.com'
PASSWORD = 'Testing1@'

def sendEmail():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(EMAIL_ADDRESS, PASSWORD)

    msg = MIMEMultipart()

    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = ""

    msg.attach(MIMEText("THIS IS A TEST EMAIL TO SEE IF IT WORKS :)", 'plain'))

    server.send_message(msg)

    server.quit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/login/login', methods=['GET','POST'])
def login():
    username = request.form.get('username')
    sequence = request.form.get('gridSequence')

    username = username.lower()

    if dbmain.loginValidation(username, sequence) == 1:
        userId = dbmain.getUserIdByUsername(username)
        sendEmail()
        # generate login token
        # dbmain.login
        # get user id
        return render_template('home.html')
    else:
        return render_template('index.html')
        
@app.route('/register')
def register(error=''):
    return render_template('registration.html',error=error)

@app.route('/register/selection', methods=['GET', 'POST'])
def selection():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    sequence = request.form.get('gridSequence')
    sequenceLength = request.form.get('tilesClicked')

    username = username.lower()
    print(sequenceLength)

    if int(sequenceLength) > 3 and not dbmain.userExistsCheck(username):
        dbmain.addNewAccount(username, fullname, email, sequence)
        return render_template('index.html')
    else:
        error = "Fill in all fields and check that number of tiles clicked is at least 4."
        return redirect(url_for('register'))
        # return register(error)
@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run()