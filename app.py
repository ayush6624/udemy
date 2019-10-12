import os
from flask import Flask, render_template, url_for, send_from_directory, request, session, redirect
import pymongo
import bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
a = os.environ.get("MONGO_URI")
mongo = pymongo.MongoClient(a)


@app.route('/')
def index():
    ##
    if 'email' in session:
        return "you are logged in as " + session['email']
    ##
    return render_template('index.html')


@app.route('/assets/<path:path>')
def css(path):
    return send_from_directory('assets', path)


@app.route('/<course>/<submodule>/<course_num>')
def find_corese(course, submodule, course_num):
    return render_template('course.html', course=course, submodule=submodule, course_num=course_num)

# Account management
@app.route('/accounts')
def show_login():
    return render_template("accounts.html")


@app.route('/accounts/<action>', methods=['POST', 'GET'])
def login(action):
    if(action == "login"):
        if request.method == 'POST':
            email = request.form["login"]  # use #name value here
            password = request.form["password"]
            # s = (f"The email {email} is successfully registered with us. Password{password}")
            users = mongo.udemy.users
            login_user = users.find_one({"email": email})

            if login_user:
                orig_pass = login_user['password']  # no need to encode it as already in bytes
                if bcrypt.hashpw(password.encode('utf-8'), orig_pass) == orig_pass:
                    session['email'] = email
                    return redirect('/')
                return "Invalid username/password combination"
            return "invalid username"
    if (action == "signup"):
        if request.method == 'POST':
            email = request.form["signup_email"]  # use #name value here
            return render_template("signup.html", email=email)


@app.route('/accounts/signup/new', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        users = mongo.udemy.users
        existing_user = users.find_one({'email': request.form['login']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email': request.form['login'], 'password': hashpass})
            session['email'] = request.form['login']
            return redirect(url_for('index'))
        return "already exists"
    return redirect('index')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.secret_key = "ayushgoyal"
    app.run(debug=True, host='0.0.0.0', threaded=True)
