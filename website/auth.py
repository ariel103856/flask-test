from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    if len(username) < 2:
        flash('Username must be longer then 1 characters')
    elif len(password1) < 8:
        flash('Password must be at least 8 characters')
    elif password1 != password2:
        flash('Passwords don\'t match')
    else:
        pass
    return render_template('signup.html')