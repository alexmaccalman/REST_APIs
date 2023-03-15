from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Define a secret key for CSRF protection
app.config["SECRET_KEY"] = "secret"

# Define a list of options for the dropdown
options = ["Fairy", "Ruprecht", "Bunny"]

# Create a form class with a dropdown pick list
class PlannerForm(FlaskForm):
    recipe_name = SelectField("Recipe Name", choices=options)
    submit = SubmitField("Submit Post")

# Define a route for the HTML page
@app.route("/", methods=["GET", "POST"])
def index():
    # Create an instance of the form class
    form = PlannerForm()
    # Initialize an empty variable for response data
    data = None
    # Check if the form is submitted and validated
    if form.validate_on_submit():
        # Get the selected value from the dropdown pick list
        selected_value = form.recipe_name.data
        # Make a REST API call to another service with the selected value as a parameter (e.g., https://example.com/api/Apple)
        response = requests.get(f"http://firstapi:8000/api/people/{selected_value}")
        # Get the JSON data from the response 
        data = response.json()
    # Render the HTML template and pass both form instance and data variable 
    return render_template("index.html", form=form, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




