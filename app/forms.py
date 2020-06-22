from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TypeIP(FlaskForm):
    ip = StringField('Type your IP or hostname.', validators=[DataRequired(), Length(min=3, max=48)])
    submit = SubmitField('Submit')