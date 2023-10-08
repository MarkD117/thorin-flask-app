import os
import json
# Importing flask class, capital f indicates a class name.
# Also imports render_template function from flask to display
# front end files. Imports request library to handle things like
# finding out what method is used and it will also hold our form
# object when we've posted it. Imports flash to display messages
# to the user on the front end
from flask import Flask, render_template, request, flash
# Importing key if file exists
if os.path.exists("env.py"):
    import env


# creating an instance of this and storing it in a variable called 'app'.
# The first argument of the Flask class, is the name of the application's
# module - our package.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# python decorator wraps function. The route decorator binds the funtion to
# itself. functions returns render_template index,html which opens the
# index.html file. The route decorator binds the funtion to itself so
# that whenever that route is called, the function is called. In this case,
# rendering the html page. This function is also called the view.
@app.route("/")
def index():
    return render_template("index.html")


# opening the company.json file as 'read' only and loading it to a variable
# called data. Argument is then assigned renaming the
# data variable to 'company'
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# view routing to the member.html page. creates an object called member
# opens the company.json file as read only and assigns it to data variable.
# For loop iterates through object checking for url value and assigning it
# to the member variable. The member.html template is then rendered.
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # The 1st member is the variable name being passed into the html file
    # The 2nd member is the member object created on line 44
    return render_template("member.html", member=member)


# methods argument allows route to accept get and post methods
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # flash displays message to the user
        flash("Thanks {}, we have received your message!".format(
            # curly brackets take the name value from the form
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


# Other arguents can be used to render server-code on the front end.
# Our custom argument 'page_title' is used to set the page title on the html
# pages. Head to the h2 element on careers.html to see how
# this information is displayed.
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# __main__ is the default module in python. It is the first one we run
if __name__ == "__main__":
    # Then we will run our app with the arguments passed in the statement below
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # Debug should only be true when testing application
