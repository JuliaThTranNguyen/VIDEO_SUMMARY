from flask import Flask, send_from_directory,render_template
from flask_cors import CORS, cross_origin
from app._init_ import app

#this api route is just a protocol shows how to gisplay flask in react
#this can be change, or delete
@app.route('/api',methods=['GET'] )
def index():
    return {
        "article":       "Welcome to heroku-this is the reply from Flask",
        "name ":         "hien tran",
        "age":           "22"
    }

# keep this one
@app.route('/')
def home_form():
    return render_template("public/home.html")
def serve():
    return send_from_directory(app.static_folder, 'index.html')

##this home route and api route here give you a view 
#on how flask and react is running together
# things can be change here, to match your purpose