import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
    )

if __name__== "__main__":
    app.run(debug=True)

