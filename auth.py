from threading import ThreadError
import website
from flask import Blueprint # use blueprint to separe the files 
from flask import render_template
from flask import request 
from flask import flash


class Logall: 

    def __init__(self, auth):
        self.auth = auth

    auth = Blueprint('auth', __name__) # defining a blueprint

    @auth.route('/login', methods=['GET', 'POST'])
    def login(self ):
        return render_template("login.html", text="Testing")

    @auth.route('/logout')
    def logout(self):
        return "<p>Logout</p>"

    @auth.route('/sign-up', methods=['GET', 'POST'])
    def sign_up(self):
        if request.method == 'POST':
          email = request.form.get('email')
          firstName = request.form.get('firstName')
          password1 = request.form.get('password1')
          password2 = request.form.get('password2')

        if len(email) < 4:
            flash ('Email must be greater than 3 characters.', category = 'error')
        elif len (firstName) < 2:
                flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
                flash('Passwords dont\'t match.', category='error')
        elif len (password1) < 7:
                flash ('Password must be at least 7 characters.', category='error')
        else:
                flash('Account created!', category='success')
        return render_template("sign_up.html")