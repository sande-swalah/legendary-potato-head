from flask import Flask

# creates the web app
app = Flask(__name__)

# Decorator: Python syntax that modifies a function; used to attach routes to views
@app.route("/")   # defines a URL
def home():       # function that runs when URL is visited
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
