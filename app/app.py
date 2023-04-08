import os
from flask import Flask, render_template, request, flash
from forms import ReservationForm
import smtplib
import ssl
from email.message import EmailMessage

port = os.getenv("MAIL_PORT")
smtp_server = os.getenv("MAIL_SERV")
sender_email = os.getenv("MAIL_ADDR")
password = os.getenv("MAIL_PASS")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "verysecretkeyforflask")


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = ReservationForm()
    if request.method == "POST":
        if form.validate() == False:
            flash("Bitt Eingabe überprüfen!")
        else:
            msg = EmailMessage()
            msg.set_content(
                f"Hallo {form.name.data},\n\nwir haben deine Anfrage erhalten und werden uns bald bei dir melden!\n\nGruss, Erikas Secret"
            )
            msg["Subject"] = "Reservationsanfrage Erikas Secret"
            msg["From"] = sender_email
            msg["To"] = form.email.data

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg, from_addr=sender_email, to_addrs=form.email.data)

            flash("Reservationsanfrage erhalten! Wir melden uns bei dir.")

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
