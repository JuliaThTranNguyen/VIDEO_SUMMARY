# import os
# from random import choice
# from flask import url_for, render_template
# from app._init_ import app, ALLOWED_EXTENSIONS, APP_ROOT, UPLOAD_FOLDER
# from werkzeug.utils import secure_filename

# ##ALLOWED_FILE - uppercase and lower case letter
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# files = [f for f in os.listdir( UPLOAD_FOLDER) if os.path.isfile(f)]
# for f in files:
#   print (f)

# @app.route('/gallery',  methods=['GET', 'POST'])
# def gallery_form():
#     	return render_template("public/gallery.html")



# # for dirpath, dirs, files in os.walk("./static/uploads/"):
# # 	print (files)

# if __name__ == "__main__":
#     pass