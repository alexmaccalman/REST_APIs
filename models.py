
from datetime import datetime
from config import db, ma

# SQLAlchemy returns data as Python class instances
class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

# Marshmellow (ma)
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
