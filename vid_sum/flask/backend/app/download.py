from flask.templating import render_template_string
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from app._init_ import app, APP_ROOT, DOWNLOAD_FOLDER
import os
import pafy
import urllib.request

# app.config["Static_download"]="/vid_sum/flask/backend/vid_sum/output_video/"
# app.config["SAVE_PATH"] = "/vid_sum/flask/backend/app/static/download"


@app.route('/display_video')
def download_form():
    	return render_template("public/download.html")

@app.route('/display_video',  methods=['GET', 'POST'])
def up_download_video():
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
		    file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
		    flash('Video ' + filename + 'is successfully uploaded and displayed.')
		    return render_template("public/download.html", filename=filename)
    return render_template("public/download.html")



#'display -video ' route
@app.route('/display_video/<filename>')
def play_video(filename):
	return redirect(url_for('static', filename='download/' + filename), code=301)

if __name__ == "__main__":
    pass