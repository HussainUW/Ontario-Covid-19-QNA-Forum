from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from datetime import datetime

class PostForm(FlaskForm):
	title = StringField('Title', validators = [DataRequired()])
	content = TextAreaField('Content', validators = [DataRequired()])
	submit = SubmitField('Post')

class AddCommentForm(FlaskForm):
	responder = StringField("Responder", validators=[InputRequired()])
	body = TextAreaField("Body", validators=[InputRequired()])
	submit = SubmitField("Post")
