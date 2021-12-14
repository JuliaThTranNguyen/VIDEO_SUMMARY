from app._init_ import app
from flask import render_template
@app.route('/about')
def about():
    	return render_template("public/about.html")

if __name__ == "__main__":
    pass