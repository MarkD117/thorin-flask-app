import os
# Importing flask class, capital f indicates a class name.
# Also imports render_template function from flask
from flask import Flask, render_template

# creating an instance of this and storing it in a variable called 'app'.
# The first argument of the Flask class, is the name of the application's
# module - our package.
app = Flask(__name__)


# python decorator wraps function. The route decorator binds the funtion to
# itself. functions returns render_template index,html which opens the
# index.html file
@app.route("/")
def index():
    return render_template("index.html")


# The route decorator binds the funtion to itself so that whenever that
# route is called, the function is called. In this case, rendering the
# html page. This function is also called the view.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# __main__ is the default module in python. It is the first one we run
if __name__ == "__main__":
    # Then we will run our app with the arguments passed in the statement below
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # Debug should only be true when testing application
