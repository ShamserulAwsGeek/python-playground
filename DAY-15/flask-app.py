from flask import Flask

#creating a flask app instance
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
app.run("127.0.0.1:5000")