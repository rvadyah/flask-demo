from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/hello/<username>")
def hello_user(username):
    return "Hey {}".format(username)