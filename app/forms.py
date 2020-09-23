from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class TypeIP(FlaskForm):
    field_data = StringField('Type  IP or hostname.', validators=[DataRequired(), Length(min=3, max=48)])
    submit = SubmitField('Check')
    ping = SubmitField('Ping')







