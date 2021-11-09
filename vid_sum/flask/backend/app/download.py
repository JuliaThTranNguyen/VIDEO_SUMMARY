from flask.templating import render_template_string
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from app._init_ import app, APP_ROOT, DOWNLOAD_FOLDER
import os
import pafy
import urllib.request

	
#'download' route
@app.route('/download_vid', methods=['POST', 'GET'])
def download():
	return render_template('public/download.html')

def checking_video():
    if request.method == 'POST':
		
		# check if the post request has the file part
	    if 'file' not in request.files:
		    flash('No file part')
		    return redirect(request.url)
	    file = request.files['file']
	    if file.filename == '':
		    flash('No image selected for uploading')
		    return redirect(request.url)
	    else:
		    filename = secure_filename(file.filename)
		    flash('File : ' + filename + 'Ready to download !')
		    return redirect(url_for('.download_vid') + filename, code=301)
	


def download_vid(filename):
	if request.method == 'GET':


 		return 'nothing done yet'
def send_video(filename):
    download = os.path.join(APP_ROOT, app.config['DOWNLOAD_PATH'])
    return send_from_directory(directory=download, filename=filename)

