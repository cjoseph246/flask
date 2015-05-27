from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Chuck'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in NYC!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Sailing on the Hudson!'
        }
    ]
    return render_template('index.html',
                           user=user,
                           posts=posts)