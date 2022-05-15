from flask_login import login_user, logout_user
from . import auth
from flask import render_template,request,redirect,url_for,flash
from app.models import User
import re


from werkzeug.security import generate_password_hash,check_password_hash

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@auth.route('/login',methods = ['GET','POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username = username).first()

        if user:
            if check_password_hash(user.password,password):
                login_user(user,remember=True)
                return redirect(url_for("main.index"))

            else:
                flash("password is wrong",category="error")
        else:
            flash("no such user", category="error")


    return render_template('auth/login.html')



@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password")
        password2 = request.form.get("password2")
        
        email_found = User.query.filter_by(email = email).first()
        username_found =  User.query.filter_by(username = username).first()


        if email_found:
            flash('Email already in use',category="error")
        elif username_found:
            flash('Username is already in user', category = 'error')
        elif password1 != password2:
            flash("Psswords must match",category = "error")
        elif len(username) < 2 and len(username) > 15:
            flash("Username must be between 2 and 15 letters",category = "error")
        elif len(password1) < 8 and len(password1) > 12:
            flash("Password must be between 8 and 12")
        elif len(password2) < 8 and len(password2) > 12:
            flash("confirm password must be between 8 and 12")

        elif not re.fullmatch(regex,email):
            flash("please enter a valid email",category="error")

        else:
            new_user = User(username = username,email = email,password = generate_password_hash(password1,method='sha256'))
            new_user.save_user()

            
            flash("Account created successfully",category='True')

            return redirect(url_for('auth.login'))

        
        
    return render_template('auth/signup.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    