from flask import Flask

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h1> Hello World! </h1>"

