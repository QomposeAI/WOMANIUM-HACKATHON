import os
#import requests
import logging

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



#headers = {
#    'Key': 'FOgbsGOPiC0Pf2DcMsn9oZDG6301428b',
#}

#@app.route("/upload_video", methods=["GET", "POST"])
#def upload_video():
#    if request.method == "POST":
#        if request.files:
#            video = request.files["video"]
#            files = {
#                'file': open(video, 'rb')
#            }
#            response = requests.post('https://muse.ai/api/files/upload', headers=headers, files=files)
#
#            return redirect(request.url)
#    return render_template("templates/index.html")

