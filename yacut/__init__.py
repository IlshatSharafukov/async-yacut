from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config


app = Flask(__name__, static_folder='../html')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from yacut import models
from yacut import views, api_views, file_views, error_handlers