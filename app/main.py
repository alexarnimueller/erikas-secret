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
        if not form.validate_on_submit():
            app.logger.info(
                f"contact form not validated for {form.name.data} {form.seats.data} {form.email.data} {form.date.data}"
            )
        else:
            app.logger.info(
                f"contact form validated for {form.name.data} {form.seats.data} {form.email.data} {form.date.data}"
            )
            content = f"""
    Hoi {form.name.data}
    
    Danke für deine Anfrage. Wir werden dir deine Reservation innerhalb von 24h bestätigen,
    sobald wir dich und deine Gäste im Sitzplan eingetragen haben.

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
            subject = f"Reservationsanfrage Erikas Secret - {form.date.data} 19:00"
            msg1 = EmailMessage()
            msg1.set_content(content)
            msg1["Subject"] = subject
            msg1["From"] = sender_email
            msg1["To"] = form.email.data

            msg2 = EmailMessage()
            msg2.set_content(f"Reservationsanfrage von {form.name.data}:\n\n" + content)
            msg2["Subject"] = subject
            msg2["From"] = sender_email
            msg2["To"] = sender_email

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg1, from_addr=sender_email, to_addrs=form.email.data)
                server.send_message(msg2, from_addr=sender_email, to_addrs=sender_email)
                app.logger.info(f"email sent to {form.email.data}")

            return redirect(url_for("yum"))

    return render_template("index.html", form=form)


@app.route("/yum", methods=["GET"])
def yum():
    return render_template("yum.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
