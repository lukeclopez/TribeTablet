from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=['POST'])
def play():
    tribe = request.form['tribe']
    return render_template("play.html",
                           tribe=tribe,
                           )

