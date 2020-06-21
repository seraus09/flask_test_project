from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TypeIP(FlaskForm):
    ip = StringField('Type your IP.', validators=[DataRequired()])
    submit = SubmitField('Submit')