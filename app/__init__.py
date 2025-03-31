import os
from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import LoginManager # type: ignore
from flask_bcrypt import Bcrypt # type: ignore

load_dotenv() # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get['\xa7\xe4\xf4\xfcR\x18\xcb\xee\x87\x1dt\x92\xd4l\xe2\xfc']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes