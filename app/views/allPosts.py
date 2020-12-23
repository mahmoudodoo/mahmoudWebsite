from flask import render_template
from app.models.post import Post
from app import app


# Create Explore view
@app.route('/allposts')
def allPosts():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('home.html', title='Explore', posts=posts)