from twitterclone import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    tweets = db.relationship('Tweet', backref=db.backref('author', lazy=True))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet_content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Tweet('{self.tweet_content}', '{self.date_posted}')" 
