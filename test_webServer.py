from flask import Flask, redirect, url_for
#  pip install flask to get the stuff for this

app = Flask(__name__)

# displays what will be on the home page

# routes this to be the default home page
@app.route("/")
def Home_Page():
    return " <h1>MineCraft Asset Randomizer<h1> Hello! This is the main page"
# time to learn HTML formatting hell

@app.route("/admin")
def admin():  # could be used for button redirections later on
    return redirect(url_for("Home_Page"))

# anything typed after / will be given as the name and displayed on a new page
@app.route("/<name>")  # can be passed as a parameter
def user(name):
    return f"Welcome {name}"


if __name__ == "__main__":
    app.run()

