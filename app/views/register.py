from flask.helpers import url_for
from app import app
from flask import render_template
from flask import render_template, flash, redirect
from flask_login import current_user
from app.models.user import Users
from app import db
from app.forms.register import RegistrationForm





#  Create register form View
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)