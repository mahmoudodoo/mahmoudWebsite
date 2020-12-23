from flask.helpers import url_for
from app import app
from flask import render_template, flash, redirect
from flask_login import current_user
from app.models.post import Post
from flask_login import login_required
from app import db
from app.forms.post import PostForm



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('home'))

    posts = current_user.followed_posts().all()

    return render_template("home.html", title='Home Page', form=form, posts=posts)