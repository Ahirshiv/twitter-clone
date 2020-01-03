from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# main route
@main.route('/')
def index():
    return render_template('index.html', title='It\'s what happening.')
