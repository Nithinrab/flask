
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to my website"

@app.route("/contact")
def login():
    return "contact page"

@app.route("/home")
def hello():
    return "enter home"

@app.route("/gallery")
def page():
    return "welcome to my page"
if __name__ == "__main__":
    app.run()