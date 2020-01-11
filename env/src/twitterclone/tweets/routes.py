from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from twitterclone.tweets.forms import TweetForm
from twitterclone import db
from twitterclone.models import Tweet, User
from flask_login import current_user

tweets = Blueprint('tweets', __name__)

# tweets route
@tweets.route('/tweets')
@login_required
def tweet():
    tweets = Tweet.query.all()
    return render_template('tweets.html', title='Tweets', tweets=tweets)


# new_tweet route
@tweets.route('/new-tweets', methods=['GET', 'POST'])
@login_required
def new_tweet():
    form = TweetForm()
    if form.validate_on_submit():
        tweet = Tweet(tweet_content=form.tweet.data, author=current_user)
        db.session.add(tweet)
        db.session.commit()
        return redirect(url_for('tweets.tweet'))
    return render_template('new-tweet.html', title='New Tweet', form=form)

# user tweet
@tweets.route('/user-tweet/<string:username>')
def user_tweets(username):
    user = User.query.filter_by(username=username).first_or_404()
    tweets = Tweet.query.filter_by(author=user)
    return render_template('user-tweets.html', title='User Tweets', tweets=tweets, user=user)