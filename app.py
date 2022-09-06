from flask import Flask

app = Flask(__name__)
amo = "mjá"
gorp = "myndavél"
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"+ amo + gorp

