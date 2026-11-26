from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World! I'm using Flask."
#add 1
#add 2　追記：課題5
#re add1
