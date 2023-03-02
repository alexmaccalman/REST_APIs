
from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema


# GET request
def read_all():
    people = Person.query.all()
    return people_schema.dump(people)

# PUT request 
def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

# GET request for one name
def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none() #use the .one_or_none() method to get one person, or return None if no match is found.

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

# PUT request. Update the fname with the value stored in person (lname is the key)
def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )