from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if isinstance(request.form.get('username'), str):
        print('str str!') 
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    print(type(username))
    if isinstance(request.form.get('username'), str):
        if len(username) < 2:
            flash('Username must be at least 2 characters', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            flash('User Created Successfuly!', category='success')
    return render_template('signup.html')