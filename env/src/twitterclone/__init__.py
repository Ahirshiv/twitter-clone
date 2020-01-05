from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from twitterclone.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from twitterclone.main.routes import main
    from twitterclone.users.routes import users
    from twitterclone.tweets.routes import tweets
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(tweets)

    return app
