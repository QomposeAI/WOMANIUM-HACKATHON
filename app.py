import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from _collections import deque

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")