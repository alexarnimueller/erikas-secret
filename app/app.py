import os
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from forms import ReservationForm


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "verysecretkeyforflask")

mail = Mail()
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERV")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_ADDR")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASS")
mail.init_app(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = ReservationForm()
    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", form=form)
        else:
            msg = Message(form.subject.data, sender=os.getenv("MAIL_ADDR"), recipients=[form.email.data])
            msg.body = """ 
                To: %s <%s> 
                Hallihallo 
            """ % (
                form.name.data,
                form.email.data,
            )
            mail.send(msg)
            flash("Reservationsanfrage erhalten! Wir melden uns bei dir.")
            form = ReservationForm()
            return render_template("index.html", form=form)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
