from monitor import Monitor
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    m = Monitor()
    word = m.get_a_word()
    return "<p>Hello, World!</p>" + word
