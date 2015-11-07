from app import app
from flask.ext.sqlalchemy import SQLAlchemy

app.secret_key='219X0XU2L0d0rxf9X168PWLx9072blbr'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://davidnnck:likenoother@localhost/pythonhunt'
app.config.from_object('config')
db = SQLAlchemy(app)