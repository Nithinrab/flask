
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1> welcome </h1>"

@app.route("/contact")
def login():
    return render_template("contact.html")

@app.route("/home")
def hello():
    return "enter home"

@app.route("/gallery")
def page():
    return "welcome to my page"
if __name__ == "__main__":
    app.run()