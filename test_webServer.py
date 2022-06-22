from flask import Flask, redirect, url_for, render_template, request
import os
from main import ignored_textures_default, randomize, ignored_sounds_default, can_randomize, ignored_music_default
from main import halt_download

#  pip install Flask-Dropzone
#  pip install flask to get the stuff for this
folderDir = ""
app = Flask(__name__)


# displays what will be on the home page
# Get = insecure way of getting info
# Post = secure way of getting info from user
# routes this to be the default home page
@app.route("/")
def Home_Page():
    return render_template("index.html", content=[])


@app.route("/About_Us")
def About_Us():
    return render_template("About_Us.html")


@app.route("/Randomize", methods=["POST", "GET"])
def Randomize():
    # randomize before this point or the death of all of us begins
    if request.method == "POST":
        return render_template("randomize.html")
    else:
        return render_template("randomize.html")


# background process happening without any refreshing
@app.route('/Randomize/<Ver_Name>')
def background_process_randomize(Ver_Name):
    if Ver_Name == "1.19":
        print("can_Randomize = ", can_randomize)
        while not can_randomize:
            continue
        halt_download()  # needed if someone is already downloading something
        randomize(str(Ver_Name), ignored_textures_default, ignored_music_default, ignored_sounds_default)
    return render_template("Download.html")


# still need to learn why
if __name__ == "__main__":
    app.run(debug=True)
