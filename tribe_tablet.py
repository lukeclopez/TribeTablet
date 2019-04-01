from flask import Flask, render_template, request
import tribes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=['POST'])
def play():
    chosen_tribe = None
    for tribe in tribes.tribes_list:
        if tribe.name == request.form['tribe']:
            chosen_tribe = tribe
    return render_template("play.html",
                           chosen_tribe=chosen_tribe,
                           )

