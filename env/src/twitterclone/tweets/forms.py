from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class TweetForm(FlaskForm):
    tweet = TextAreaField('Tweet', validators=[DataRequired()])
    submit = SubmitField('Submit')
