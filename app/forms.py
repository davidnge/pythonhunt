from wtforms import Form, StringField, BooleanField, validators

class suggestForm(Form):
	title = StringField('Title')
	category = StringField('Category')
	url = StringField('URL Field', [validators.URL(message='Sorry, this is not a valid URL')])
	description = StringField('Description')
	email = StringField('Email', [validators.Optional(), validators.Email()])

