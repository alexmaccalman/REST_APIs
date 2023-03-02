
import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve() # creates the variable basedir pointing to the directory that the program is running in.
connex_app = connexion.App(__name__, specification_dir=basedir) # uses the basedir variable to create the Connexion app instance and give it the path to the directory that contains your specification file.

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)