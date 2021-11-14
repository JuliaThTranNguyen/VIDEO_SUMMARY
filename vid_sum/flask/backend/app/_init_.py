from flask import Flask
from os.path import join, dirname, realpath
import os
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'static/uploads/'
DOWNLOAD_FOLD = 'static/download'


UPLOADS_PATH = os.path.join(APP_ROOT, UPLOAD_FOLD)
DOWNLOAD_PATH = os.path.join(APP_ROOT, DOWNLOAD_FOLD)

UPLOAD_FOLDER = UPLOADS_PATH 
DOWNLOAD_FOLDER = DOWNLOAD_PATH

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

APP_ROOT =os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] =  2024 * 2024 * 2024

app.config['TESTING'] = True
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)


from app import uploads
from app import download
from app import gallery



# from __the main directory__ import the __python _file __