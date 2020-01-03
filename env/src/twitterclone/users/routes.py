from flask import Blueprint, render_template, url_for, redirect
from twitterclone.users.forms import Signup, Login

users = Blueprint('users', __name__)

# signup route
@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()
    if form.validate_on_submit():
        return redirect(url_for('users.login'))
    return render_template('signup.html', title='Sign up for Twitter-Clone', form=form)


# login route
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@demo.com' and form.password.data == '1234':
            return redirect(url_for('tweets.tweet'))
    return render_template('login.html', title='Login on Twitter-Clone', form=form)
