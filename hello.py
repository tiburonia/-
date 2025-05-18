from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/")
def index():
    return render_template("hello.html", name="게스트")