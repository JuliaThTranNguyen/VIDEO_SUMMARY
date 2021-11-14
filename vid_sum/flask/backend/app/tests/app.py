# app/tests/

############################
#### setup and teardown ####
############################
import base64
import os
import pathlib
import tempfile
import textwrap
import unittest

import flask
from flask import app
import werkzeug.utils
from flask import request
from io import StringIO
from werkzeug.utils import secure_filename

root = flask.Blueprint('root', __name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/vid_sum/flask/backend/app/static/uploads/'

UPLOADS_PATH = os.path.join(APP_ROOT, UPLOAD_FOLD)

UPLOAD_FOLDER = UPLOADS_PATH 
root.config = ["UPLOAD_FOLDER"]#tempfile.gettempdir()


@root.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if flask.request.method == 'POST':
        try:
            file = flask.request.files['file']
            if not file.filename:
                raise LookupError()
            filename = werkzeug.utils.secure_filename(file.filename)
            file.save(pathlib.Path(flask.current_app.config['UPLOAD_FOLDER'], filename))
            flask.flash('File saved!' + filename)
        except LookupError:
            flask.flash('No file provided!', 'error')
        return flask.redirect(flask.url_for('root.upload_file'))
    else:
        return flask.render_template_string(textwrap.dedent(
            '''\
            <!doctype html>
            <title>Upload new File</title>
            {% with messages = get_flashed_messages(with_categories=true) %}{% if messages %}
            <ul class=flashes>
            {% for category, message in messages %}<li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
            {% endif %}{% endwith %}
<div style="margin: 10px auto;">
    <video autoplay="autoplay" controls="controls" preload="preload">
			<source src="{{ url_for('display_video', filename=filename) }}" type="video/mp4"></source>
	</video>
</div>
{% endif %}
<form method="post" action="/uploads" enctype="multipart/form-data">
    <dl>
        <p>
            <input type="file" name="file" autocomplete="off" required>
        </p>
    </dl>

    <form name="myForm" action="" method="post" onsubmit="">
        <p>
            <input type="submit" value="Upload"> <br>
        </p>
    </form>
</form>
            '''
        ))
print("Test for Upload_file completed! OK.    run from: app.py")

def create_app():
    app = flask.Flask(__name__)
    app.config['UPLOAD_FOLDER'] = tempfile.gettempdir() #tempfile.gettempdir()
    app.secret_key = 'change-me'
    app.register_blueprint(root)
    return app

if __name__ == '__main__':
    create_app()
    