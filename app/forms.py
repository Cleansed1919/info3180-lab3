from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name (Required)', validators=[InputRequired()])
    email = StringField('Email (Required)', validators=[InputRequired(), Email()])
    subject = StringField('Subject (Required)', validators=[InputRequired()])
    message = StringField('Message (Required)', validators=[InputRequired()])
    submit = SubmitField('Send')