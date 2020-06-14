from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import IPAddress

class TypeIP(FlaskForm):
    ip = StringField('Type your IP.', validators=[IPAddress()])
    submit = SubmitField('Submit')