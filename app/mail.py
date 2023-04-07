#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import smtplib
import ssl
from email.message import EmailMessage

port = os.getenv('MAIL_PORT')
smtp_server = os.getenv('MAIL_SERV')
sender_email = os.getenv('MAIL_ADDR')
password = os.getenv('MAIL_PASS')

recipient_email = sender_email
recipient_name = "Erikas"

msg = EmailMessage()
msg.set_content(f"Hallo {recipient_name},\n\nwir haben deine Anfrage erhalten und werden uns bald bei dir melden!\n\nGruss, Erikas Secret")
msg['Subject'] = "Reservationsanfrage Erikas Secret"
msg['From'] = sender_email
msg['To'] = recipient_email

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(msg, from_addr=sender_email, to_addrs=recipient_email)

