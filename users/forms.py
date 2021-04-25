from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from Flask_Blog.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[
		DataRequired(message=('Please enter a username')), 
		Length(min=2, max=20, message=('Username must be between 2 and 20 characters'))
		])
	email = StringField('Email', validators=[
		DataRequired(message=('Please enter an email')), 
		Email(message=('Please enter a valid email'))
		])
	password = PasswordField('Password', validators=[
		DataRequired(message=('Please enter a password'))
		])
	confirm_password = PasswordField('Confirm Password', validators=[
		DataRequired(message=('Please re-enter your password')), 
		EqualTo('password', message=('Passwords do not match'))
		])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('An account has already been made with that email. Please use a different one.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[
		DataRequired(message=('Please enter an email')), 
		Email(message=('Please enter a valid email'))
		])
	password = PasswordField('Password', validators=[
		DataRequired(message=('Please enter a password'))
		])
	remember = BooleanField('Remember Me') 
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[
		DataRequired(message=('Please enter a username')), 
		Length(min=2, max=20, message=('Username must be between 2 and 20 characters'))
		])
	email = StringField('Email', validators=[
		DataRequired(message=('Please enter an email')), 
		Email(message=('Please enter a valid email'))
		])
	picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('An account has already been made with that email. Please use a different one.')

class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[
		DataRequired(message=('Please enter an email')), 
		Email(message=('Please enter a valid email'))
		])
	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email, you must register first.')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[
		DataRequired(message=('Please enter a password'))
		])
	confirm_password = PasswordField('Confirm Password', validators=[
		DataRequired(message=('Please re-enter your password')), 
		EqualTo('password', message=('Passwords do not match'))
		])
	submit = SubmitField('Reset Password')
