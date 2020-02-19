from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
# app.secret_key = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/register/selection', methods=['GET', 'POST'])
def selection():
    imageValue = request.form.get('imageToUse')
    print(imageValue)

    if imageValue == str(1):
        imageToDisplay = "../static/images/cat_grid.jpg"
    elif imageValue == str(2):
        imageToDisplay = "../static/images/duck.jpg"
    else:
        imageToDisplay = "../static/images/tiger.jpg"

    print(imageToDisplay)

    return render_template('selection.html', imageToDisplay = imageToDisplay)

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run()