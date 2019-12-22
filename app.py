import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    return "<br>".join(messages)


@app.route("/", methods=["GET", "POST"])
def index():
    """main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

# if user enters there user name we will return welcome plus the username
@app.route("/<username>")
def user(username):
    """display messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

# if the user enters the user name and a message there name and a message


@app.route("/<username>/<message>")
def send_message(username, message):
    """create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == '__main__':
        # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
