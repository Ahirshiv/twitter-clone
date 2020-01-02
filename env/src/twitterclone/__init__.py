from flask import Flask
from twitterclone.config import Config
from twitterclone.main.routes import main
from twitterclone.users.routes import users

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
