import os
from flask import Flask, render_template, request, redirect, url_for
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
        if not form.validate():
            app.logger.info("contact form not validated")
        else:
            app.logger.info("contact form validated")
            msg = EmailMessage()
            msg.set_content(
                f"""Hoi {form.name.data}
                Danke für deine Anfrage. Wir werden dir deine Reservation innerhalb von 24h bestätigen, sobald wir dich und deine Gäste im Sitzplan eingetragen haben.

                Name:   {form.name.data}
                Plätze: {form.seats.data}
                E-Mail: {form.email.data}
                Datum:  {form.date.data}
                Zeit:   19:00


                Fragen oder Änderungen?
                erikasdiner@gmail.com

                Bis bald
                Erika
                """
            )
            msg["Subject"] = "Reservationsanfrage Erikas Secret"
            msg["From"] = sender_email
            msg["To"] = form.email.data

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg, from_addr=sender_email, to_addrs=form.email.data)
                app.logger.info(f"email sent to {form.email.data}")

            return redirect(url_for("yum"))

    return render_template("index.html", form=form)


@app.route("/yum", methods=["GET"])
def yum():
    return render_template("yum.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
