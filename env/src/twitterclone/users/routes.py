from flask import Blueprint, render_template, url_for

users = Blueprint('users', __name__)

# signup route
@users.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', title='Sign up for Twitter-Clone')


# login route
@users.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login on Twitter-Clone')
