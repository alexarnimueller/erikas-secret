#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, NumberRange


class ReservationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Bitte gib deinen Namen ein.")])
    email = StringField(
        "Email", validators=[DataRequired(message="Bitte gib eine gültige Email Adresse ein."), Email()]
    )
    seats = StringField(
        "Plätze",
        validators=[
            DataRequired(message="Bitte gib die Anzahl Plätze ein."),
            NumberRange(1, 10, message="Maximal 10 Plätze pro Person möglich."),
        ],
    )
    date = RadioField(
        "Datum",
        choices=[("26.4.", "26.4."), ("27.4.", "27.4."), ("3.5.", "3.5."), ("4.5.", "4.5.")],
        validators=[DataRequired(message="Bitte wähle ein Datum aus.")],
    )
    submit = SubmitField("Send")
