#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired


class ReservationForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired(message="Bitte gib deinen Namen ein.")], render_kw={"placeholder": "Name"}
    )
    email = StringField(
        "Email",
        validators=[DataRequired(message="Bitte gib eine gültige Email Adresse ein."), Email()],
        render_kw={"placeholder": "Email"},
    )
    seats = StringField(
        "Plätze",
        validators=[DataRequired(message="Bitte gib die Anzahl Plätze ein.")],
        render_kw={"placeholder": "Plätze"},
    )
    date = RadioField(
        "Datum",
        choices=[("26.4.", "26.4."), ("27.4.", "27.4."), ("3.5.", "3.5."), ("4.5.", "4.5.")],
    )
    submit = SubmitField("OK")
