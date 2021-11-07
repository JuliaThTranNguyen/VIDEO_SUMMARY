from flask import Flask
from os.path import join, dirname, realpath
import os
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment



UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/')
UPLOAD_FOLDER = UPLOADS_PATH 
DOWNLOAD_PATH = UPLOADS_PATH
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

APP_ROOT =os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] =  2024 * 1024 * 1024

app.config['TESTING'] = True
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)


from app import routing
from app import testing_with_react



