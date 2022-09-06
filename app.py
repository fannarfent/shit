from flask import Flask

app = Flask(__name__)
amo = "mjá"
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"+ amo 

