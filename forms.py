from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, URL

class suggestForm(Form):
	url = StringField('URL Field', [validators.URL(message='Sorry, this is not a valid URL')])
	description = StringField()
