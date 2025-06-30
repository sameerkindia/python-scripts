from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, Sameer!</p>"s

@app.route("/")
def home():
 return render_template('index.html')

@app.route("/<username>")
def userpage(username=None):
 return render_template('index.html' , name=username)