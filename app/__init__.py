from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
from models import Directory
from config import db

admin = Admin(app, template_mode='bootstrap3')
admin.add_view(ModelView(Directory, db.session))


from app import views
