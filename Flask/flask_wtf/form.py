from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField
from wtforms.validators import DataRequired , Email, Length

class RegForm(FlaskForm):
    name = StringField("Full Name" , validators=[DataRequired()])
    email = StringField("Email" , validators=[DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField("Password" , validators=[DataRequired(),Length(min=6)])
    submit = SubmitField("Register")
