from flask import Flask, render_template, request, session, make_response
from static.database.database import Database
app = Flask(__name__)
# app.secret_key = ''

dbmain = Database()

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
        # generate login token
        # dbmain.login
        # get user id
        return render_template('home.html')
    else:
        return render_template('index.html')
        
@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/register/selection', methods=['GET', 'POST'])
def selection():
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    email = request.form.get('email')
    sequence = request.form.get('gridSequence')

    if not dbmain.userExistsCheck(username):
        dbmain.addNewAccount(username, fullname, email, sequence)
        return render_template('index.html')
    else:
        return render_template('login.html') #THIS HAS TO BE CHANGED ================================================ADFADFADF=AD=FA=DFA=F=ASDF=AD=FA=F=AF=ASF=A=F=ASF=ASDF=

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run()