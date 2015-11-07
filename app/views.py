
from app import app
from flask import render_template, request, url_for, redirect, session, flash
from functools import wraps
from forms import suggestForm
from models import Directory, Category
from config import db



@app.route('/')
def index():

	d = Directory.query.all()
	return render_template('base.html', directories = d)

@app.route('/success')
def success():
	return render_template('success.html')


@app.route('/suggest', methods=['GET', 'POST'])
def suggest():
	form = suggestForm(request.form)
	if form.validate():
		title = form.title.data
		url = form.url.data
		desc = form.description.data
		email = form.email.data
		cat = form.category.data

		new_dir = Directory(url, title, desc, cat)
		db.session.add(new_dir)
		db.session.commit()

		return redirect(url_for('index'))


	else:
		print 'wrong input'

	return render_template('suggest.html', form=form)


	


if __name__== '__main__':
	app.run(debug=True)


