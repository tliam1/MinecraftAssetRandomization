from flask import Flask, redirect, url_for, render_template
#  pip install flask to get the stuff for this

app = Flask(__name__)

# displays what will be on the home page

# routes this to be the default home page
@app.route("/")
def Home_Page():
    return render_template("index.html", content=["Dream", "SnapNap", "George Not Found"])

@app.route("/admin")
def admin():  # could be used for button redirections later on
    return redirect(url_for("Home_Page"))

# anything typed after / will be given as the name and displayed on a new page
# @app.route("/<name>")  # can be passed as a parameter
# def user(name):
#     return f"Welcome {name}"


# still need to learn why
if __name__ == "__main__":
    app.run(debug=True)

