from flask import Flask

app = Flask(__name__)

# To view what's on the Flask site, run the following command in CMD:
# $env:FLASK_APP = "api.py"
# $env:FLASK_ENV = "development"
# flask run

@app.route('/')
def index():
    return 'Hello!'