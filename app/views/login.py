from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from flask_login import logout_user,login_user,current_user
from app.forms.login import LoginForm
from app.models.user import Users

# Create login form view
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)



# Create Log out function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
