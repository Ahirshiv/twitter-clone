from flask import Blueprint, render_template
from flask_login import login_required

tweets = Blueprint('tweets', __name__)


# dummy tweets
total_tweets = [
    {
        'username': 'SatyamKY',
        'tweet': 'Twitter-Clone is awesome place for programmers! :)'
    },
    {
        'username': 'YeshaPatel',
        'tweet': 'Hello Twitter-Clone users!'
    },
    {
        'username': 'ShivAhir',
        'tweet': 'I love programming. :)'
    }
]


# tweets route
@tweets.route('/tweets')
@login_required
def tweet():
    return render_template('tweets.html', title='Tweets', tweets=total_tweets)
