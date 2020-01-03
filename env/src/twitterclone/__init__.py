from flask import Flask
from twitterclone.config import Config
from twitterclone.main.routes import main
from twitterclone.users.routes import users
from twitterclone.tweets.routes import tweets

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(tweets)

    return app
