from flask import Flask, render_template
import os
app = Flask (__name__)


# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
