import os
from flask import Flask, render_template, url_for, send_file, send_from_directory, request

app = Flask(__name__)
MEDIA_PATH = os.getcwd()+'/static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/assets/<path:path>')
def css(path):
    return send_from_directory('assets', path)


@app.route('/<course>/<submodule>/<course_num>')
def find_corese(course, submodule, course_num):
    return render_template('course.html', course=course, submodule=submodule, course_num=course_num)


@app.route('/<submodule>/<vid_name>')
def serve(submodule, vid_name):
    vid_path = MEDIA_PATH + '/' + submodule + '/' + vid_name + '.mp4'
    return send_file(vid_path, 'video/mp4', conditional=True)


@app.route('/accounts', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["login"]  # use #name value here
        password = request.form["password"]
        s = (f"The email {email} is successfully registered with us.")
        return s
    return render_template('accounts.html')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
