from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Flávio'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portugal!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)