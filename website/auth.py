from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', header="This is Login page")

@auth.route('/logout')
def logout():
    return render_template('login.html', header="This is Login page")

@auth.route('/signup')
def signup():
    return render_template('signup.html', header="This is Sign Up page")