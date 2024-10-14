from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.register_login import User
from flask_app.controllers import campaign_controller
#OK to import classes here it wont hurt anything
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import render_template, redirect, request, session, flash
bcrypt = Bcrypt(app)

@app.route('/')
def default():
	return render_template ('login.html')

@app.route('/', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    print (request.form)
    data = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "password" : pw_hash,

	}
    if User.validate_register(data):  # Validate data before saving
        User.create(data)
        flash("Registration successful!")
        return redirect('/')
    else:
        return redirect('/dashboard')
    
@app.route('/')
def dashboard():
	return render_template ('dashboard.html')

@app.route('/dashboard', methods=['POST'])
def logging_in():
    data = {
    "email" : request.form.get('email'),
    "password" : request.form.get ('password'),
	}
    user = User.get_by_email({"email" :data['email']})
    if not user:
        flash("Invalid email or password.")
        return redirect('/')
    
    if not EMAIL_REGEX.match(data['email']):
        flash("Invalid email or password.")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, data['password']):
        flash("Invalid email or password.")
        return redirect('/')
    
    session['users_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')


@app.route('/log_out')
def destroy_session():
    session.clear()
    return redirect('/')