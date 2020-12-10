# Set up your imports here!
# import ...
from flask import Flask, request

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return "Welcome Page"

#http://127.0.0.1:5000/puppy-latin
@app.route('/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    return "<p>my pet name is {}</p>".format(name.replace("-"," "))

if __name__ == '__main__':
    app.run(debug=True)
