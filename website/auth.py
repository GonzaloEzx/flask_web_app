
from unicodedata import category
from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	return render_template("login.html", boolean=False)

@auth.route('/logout')
def logout():
	return "<h1>Logout</h1>"	

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		firstName = request.form.get('firstName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		if len(email) < 4:
			flash('Email must be greater than 3 character', category='error')
		elif len(firstName) < 2:
			flash('Email must be greater than 3 character', category='error')
		elif password1 != password2:
			flash('Password dont match', category='error')
		elif len(password1) < 7:
			flash('Password must be at 7 character', category='error')
		else:
			# add user to database\
			flash('Account created!', category='success')

	return render_template("sign_up.html")

