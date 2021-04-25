# imports Flask module (allows us to use the framework) and imports render_template
# module (allows us to return from html templates and pass parameters to templates)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from Flask_Blog.config import Config

# instantiates a web application called 'app'  

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_class=Config):
	app = Flask(__name__)

	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from Flask_Blog.users.routes import users
	from Flask_Blog.posts.routes import posts
	from Flask_Blog.main.routes import main
	from Flask_Blog.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app


