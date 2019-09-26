#from flask import Flask, redirect, request, make_response, render_template
from flask import *
from connection import *
import os
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)
@app.route('/')
def home():
	return render_template('index.html')

@app.route("/<a>",methods = ['GET','POST'])
def hrefmethod(a):
	if a == "login":
		return render_template('login.html')
	elif a == "register":
		return render_template('register.html')	
	elif a == "logout":
		session.pop('user', None)
		return redirect(url_for('home'))
	

@app.route("/loginauth",methods = ['GET',"POST"])
def loginauth():
	username = request.form['username_txtbox']
	password = request.form['password_txtbox']
	role = request.form['role_dropdown']
	result = db.login.find_one({"username": username, "password":password})
	if result is None:
		return "Invalid username or password"
	else:
		session['user'] = username
		session['role'] = role
		if role == "Admin" or role == "admin":
			return redirect(url_for('ownerhome',a = 'home'))
		if role == "User"  or role == "user":
			return redirect(url_for('userhome', a = 'home'))		
		
@app.route("/Register",methods = ["POST"])
def register():
	name = request.form['name_txtbox']
	username = request.form['username_txtbox']
	contact_no = request.form['ContactNo._txtbox']
	password = request.form['password_txtbox']
	try:
		db.Cryptography.insert(
			 {
			  'name': name,
			  'email': username, 
			  'number': contact_no,
			  'password': password
			  } 
			 )
		return redirect(url_for('hrefmethod',a = 'login'))
	except:		
		print("Registration Failed")

@app.before_request
def before_req():
	g.user = None
	g.role = None
	if 'user' in session:
		g.user = session['user']
	if 'role' in session:
		g.role = session['role']

@app.route('/owner/<a>', methods = ["GET","POST"])
def ownerhome(a):
	if a == "home":
		return render_template('home.html')
	elif a == "file-upload":
		return render_template('file-upload.html')
	elif a == "file-view":
		return render_template('file-view.html')
	elif a == "view-request":
		return render_template('view-request.html')
	
@app.route('/user/<a>', methods = ["GET","POST"])
def userhome(a):
	if a == "home":
		return render_template('home.html')
	elif a == "verify":
		# return render_template('verify.html')
		return " <html><h1>#</h1> </html>"
	elif a == "file-view":
		return render_template('file-view.html')
	
if __name__ == "__main__":
	app.run(debug=True)
