from flask import Flask, render_template, request, session, make_response, redirect, url_for
from static.database.database import Database
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random as random
import math as math
import datetime

app = Flask(__name__)
# app.secret_key = ''

dbmain = Database()

EMAIL_ADDRESS = 'graphical58@gmail.com'
PASSWORD = 'Testing1@'

def sendEmail(email, otp):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(EMAIL_ADDRESS, PASSWORD)

    msg = MIMEMultipart()

    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg['Subject'] = "One-Time Password Verification"

    msg.attach(MIMEText("The One Time Password is : " + otp, 'plain'))

    server.send_message(msg)

    server.quit()

def generateOTP():
    otp = ""
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stringLength = len(string)
    
    for i in range(6):
        otp += string[math.floor(random.random() * stringLength)]
    return otp

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/otp', methods=['GET','POST'])
def otppage():
        username = request.form.get('username')
        sequence = request.form.get('gridSequence')
        imageid = request.form.get('imageToUse')

        username = username.lower()

        if dbmain.loginValidation(username, sequence, imageid) == 1:
            userId = dbmain.getUserIdByUsername(username)
            email = dbmain.getEmailByUserId(userId)
            
            otp = generateOTP()
            timestamp = datetime.datetime.now().timestamp()
            dbmain.renewOtpOfUser(username, otp, str(timestamp)) #Renews the OTP and timestamp of user in database
            sendEmail(email, otp)
            
            # generate login token
            # dbmain.login
            # get user id
            return render_template('otppage.html', userid = userId)
        else:
            error = "Username and/or graphical password incorrect"
            return render_template('login.html', error=error)
        
@app.route('/otp/otp', methods=['GET','POST'])
def otp():
    formOtp = request.form.get('otp')
    userid = request.form.get('userid')
    newTimestamp = datetime.datetime.now().timestamp()         #Timestamp after form is submitted

    dbOtp = dbmain.getOtpByUserId(userid)                      #OTP from database
    dbTimestamp = float(dbmain.getTimestampByUserId(userid))   #Timestamp from database

    #If the otp entered matches with one in database and timestamp difference is less than 2 mins
    if formOtp == dbOtp and newTimestamp - dbTimestamp < 120:
        return render_template('home.html')
    else:
        return render_template('otppage.html', userid = userid)

@app.route('/otp/newOtp', methods=['GET', 'POST'])
def newOtp():
    userid = request.form.get('userid')
    username = dbmain.getUsernameByUserId(userid)
    email = dbmain.getEmailByUserId(userid)

    otp = generateOTP()
    timestamp = datetime.datetime.now().timestamp()
    dbmain.renewOtpOfUser(username, otp, str(timestamp)) #Renews the OTP and timestamp of user in database
    sendEmail(email, otp)
    return render_template('otppage.html', userid = userid)

        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        sequence = request.form.get('gridSequence')
        sequenceLength = request.form.get('tilesClicked')
        imageid = request.form.get('imageToUse')

        username = username.lower()
        print(sequenceLength)

        if int(sequenceLength) > 3 and not dbmain.userExistsCheck(username):
            dbmain.addNewAccount(username, fullname, email, sequence, imageid)

            otp = generateOTP() #Generates new OTP
            timestamp = datetime.datetime.now().timestamp()
            dbmain.addNewOtp(username, otp, str(timestamp))

            return render_template('index.html')
        else:
            error = "Invalid Credentials and/or graphical password"
            return render_template('registration.html', error=error)
            # return redirect(url_for('register'))
            # return register(error)
    else:
        return render_template('registration.html')


@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run()