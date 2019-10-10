import os
from flask import Flask, render_template, url_for, send_file, send_from_directory, request

app = Flask(__name__)
MEDIA_PATH = os.getcwd() + '/static'


@app.route('/')
def index():
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
            s = (f"The email {email} is successfully registered with us. Password{password}")
            return s
    if (action == "signup"):
        if request.method == 'POST':
            email = request.form["signup_email"]  # use #name value here
            s = (f"The email {email} is successfully registered with us.")
            return render_template("signup.html", email=email)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
