from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load .env values
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a8e3d07e60f2a7cbf234a9dff0e8f1ab'

# Mail Configuration (loaded from .env)
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT"))
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS") == "True"
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_DEFAULT_SENDER")

mail = Mail(app)

# Contact form class
class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')

# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message("New Contact Form Message",
                recipients=["munabiswal955@gmail.com"])
        msg.body = f"""Message from {form.name.data} <{form.email.data}>:

{form.message.data}
"""
        mail.send(msg)
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact", form=form)

if __name__ == "__main__":
    app.run(debug=True)
