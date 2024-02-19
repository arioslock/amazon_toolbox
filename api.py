from flask import Flask

app = Flask(__name__)

# Żeby zobaczyć co jest na stronie w cmd
# $env:FLASK_APP = "api.py"
# $env:FLASK_ENV = "development"
# flask run

@app.route('/')
def index():
    return 'Hello!'