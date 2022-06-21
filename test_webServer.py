from flask import Flask, redirect, url_for, render_template, request
from flask_dropzone import Dropzone
import os
from main import ignored_list, randomize
#  pip install Flask-Dropzone
#  pip install flask to get the stuff for this
folderDir = ""
app = Flask(__name__)
baseDir = os.path.abspath(os.path.dirname(__file__))
app.config.update(
    UPLOADED_PATH=os.path.join(baseDir, 'static'),
    DROPZONE_MAX_FILE_SIZE=2000,  # Mb
    DROPZONE_TIMEOUT=10 * 60 * 1000
)
dropzone = Dropzone(app)


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
    # if Ver_Name == "1.19":
    #     randomize(str(Ver_Name), ignored_list)
    return render_template("Download.html")


# still need to learn why
if __name__ == "__main__":
    app.run(debug=True)
