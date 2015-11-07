from config import db

class Directory(db.Model):
	__tablename__ = 'directory'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String())
	title = db.Column(db.String())
	description = db.Column(db.String())
	category = db.Column(db.String())

	def __init__(self, url, title, description, category):
		self.url = url
		self.title = title
		self.description = description
		self.category = category

	def __repr__(self):
		return self.url


class Category(db.Model):
	__tablename__ = 'category'

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String())

	def __repr__(self):
		return self.name
