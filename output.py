# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Jack"
    age = "20" 

    return render_template('index.html' , name = name , age = age)


# define the route to father webpage
@app.route("/father")
def first_webPage():

    return "MY FATHER"


# define the route to mother webpage
@app.route("/mother")
def second_webPage():

    return "MY MOTHER"



# define the route to friends webpage
@app.route("/friend")
def third_webPage():

    return "MY FRIEND"


# add other routes, if you want
@app.route("/me")
def fourth_webPage():

    return "ME"




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
