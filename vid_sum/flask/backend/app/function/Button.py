# from flask import Flask, request, render_template,redirect,url_for
# from werkzeug.datastructures import ContentSecurityPolicy
# from app._init_ import app
# import cgi, cgitb 



# @app.route("/", methods=['GET','POST'])
# def get_value():
#     value={0}
#     if request.method == 'POST':
# #Create instance of FieldStorage 
#      form = cgi.FieldStorage() 


# # Get data from fields
#      if form.getvalue('subject') :
#         subject = form.getvalue('subject')
#         value += subject
#      else:
#         subject = "Not set"
#         print(subject)
#      return subject
    
#     return redirect(url_for("value", video_length=value))

# @app.route("/<get_value>")
# def value(video_length):
#     	return f"<h1>{video_length}</h1>"


