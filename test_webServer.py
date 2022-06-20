from flask import Flask, redirect, url_for, render_template, request
#  pip install flask to get the stuff for this
folderDir = ""
app = Flask(__name__)

# displays what will be on the home page
# Get = insecure way of getting info
# Post = secure way of getting info from user
# routes this to be the default home page
@app.route("/")
def Home_Page():
    return render_template("index.html", content=["Dream", "SnapNap", "George Not Found"])

@app.route("/About_Us")
def About_Us():
    return render_template("About_Us.html")

@app.route("/Randomize", methods=["Post", "Get"])
def Randomize():
    if request.method == "POST":
        # when pressing submit do something
        temp = request.form["asset_dir"]
        listOfGlobals = globals()  # only way to assign new values to "Undetermined value" globals
        listOfGlobals['folderDir'] = temp
        print(folderDir)
        return redirect(url_for("Randomizer_Success"))
    else:
        return render_template("randomize.html")

@app.route("/Successful_Randomization")
def Randomizer_Success():
    return f"<h1>Randomization Sucessful! You can now close this page!</h1>\n" \
           f"<p>Base Assets Folder Location: {folderDir}</p>\n" \
           f"<p>Randomized Assets Folder Location: enter Dir here"


# still need to learn why
if __name__ == "__main__":
    app.run(debug=True)
