from flask import Blueprint, render_template

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
    }
]


# tweets route
@tweets.route('/tweets')
def tweet():
    return render_template('tweets.html', title='Tweets', tweets=total_tweets)
