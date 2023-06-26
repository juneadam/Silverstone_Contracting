"""
A server file for SILVERSTONE CONTRACTING & Landscaping 
"""
from flask import Flask, render_template, redirect, request, flash, session
import jinja2
from flask_mail import Mail, Message
from forms import ContactForm
# from model import db
# from model import Routine, User, Exercise, PracticeSession, db
# from crud import last_two_sessions, get_user_by_id
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "justferfunan@gmail.com"
app.config["MAIL_PASSWORD"] = "ztwfbdblwefbfdck"
mail.init_app(app)

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def landing():
    """Return homepage."""

    return render_template("landing.html")

@app.route("/about")
def about():
    """Return about page."""

    return render_template("about.html")

@app.route("/services")
def services():
    """Return services page."""

    return render_template("services.html")

@app.route("/projects")
def projects():
    """Return projects page."""

    return render_template("projects.html")

@app.route("/contacts", methods=["GET", "POST"])
def contact():
    """Return contact page."""
    form = ContactForm()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('contacts.html', form=form, success=False)
        else:
            msg = Message("Silverstone Web Form Request", sender='justferfunan@gmail.com', recipients=['justferfunan@gmail.com'])
            msg.body = f"From: {form.name.data} <{form.email.data}>\n{form.message.data}"
            mail.send(msg)
            return render_template("contacts.html", form=form, success=True)
    elif request.method == 'GET':
        return render_template("contacts.html", form=form, success=False)



if __name__ == "__main__":
    # from model import connect_to_db
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)