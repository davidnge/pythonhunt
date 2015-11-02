from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.secret_key='219X0XU2L0d0rxf9X168PWLx9072blbr'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://davidnnck:likenoother@localhost/pythonhunt'
app.config.from_object('config')
db = SQLAlchemy(app)



def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('you need to log in first')
			return redirect(url_for('login'))
	return wrap


@app.route('/')
@login_required
def index():
	return render_template('base.html')

@app.route('/success')
def success():
	return render_template('success.html')

class User(db.Model):
	__tablename__= 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, email):
		self.email = email

	def __repr__(self):
		return '<E-mail %r>' % self.email

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Wrong username and password, please try again'
		else:
			session['logged_in'] = True
			flash('you were just logged in')
			return redirect(url_for('success'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	flash('you were just logged out')

	return redirect(url_for('index'))

	


if __name__== '__main__':
	app.run(debug=True)


