from flask import Flask, redirect, url_for, render_template, request
import os
from os.path import exists
from main import ignored_textures_default, randomize, ignored_sounds_default, ignored_music_default
from main import q, can_download, mypath
import random
import threading

#  pip install Flask-Dropzone
#  pip install flask to get the stuff for this
app = Flask(__name__)

# displays what will be on the home page
# Get = insecure way of getting info
# Post = secure way of getting info from user
# routes this to be the default home page
@app.route("/")
def Home_Page():
    return render_template("index.html", content=[])


# @app.route("/About_Us")
# def About_Us():
#     return render_template("About_Us.html")


# @app.route("/Randomize", methods=["POST", "GET"])
# def Randomize():
#     # randomize before this point or the death of all of us begins
#     if request.method == "POST":
#         return render_template("randomize.html")
#     else:
#         return render_template("randomize.html")


# background process happening without any refreshing
@app.route('/Randomize/<Ver_Name>')
def background_process_randomize(Ver_Name):
    if Ver_Name == "1.19":
        client_id = random.randrange(1, 1000000, 1)
        q.put(client_id)
        # halt_download()  # needed if someone is already downloading something
        # while q.queue[0] != id:
        #     continue
        if can_download():
            client_thread = threading.Thread(target=randomize, args=(str(Ver_Name), ignored_textures_default, ignored_music_default, ignored_sounds_default, False))
            client_thread.start()
            # client_thread.join()  # join waits till thread ends before continuing
        while not exists(mypath + "/static/zipFiles/Randomized_MC_Assets.zip"):  # if removing the zip folder causes a permissions error...wait
            continue
        # randomize(str(Ver_Name), ignored_textures_default, ignored_music_default, ignored_sounds_default, False)
        # print("Running randomization because can_randomize =", can_randomize)
    return render_template("Download.html")


# still need to learn why
if __name__ == "__main__":
    app.run()
