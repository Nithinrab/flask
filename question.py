from flask import Flask, render_template

me = Flask(__name__)

@me.route("/")
def data():
    return render_template("submit.html")

@me.route("/search")
def search():
    return render_template("search.html")

@me.route("/delete")
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    me.run()