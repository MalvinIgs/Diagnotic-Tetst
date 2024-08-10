from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/igs')
def igs():
    return render_template("igs.html")

@app.route('/i')
def i():
    return render_template("i.html")

@app.route('/g')
def g():
    return render_template("g.html")

@app.route('/s')
def s():
    return render_template("s.html")

if __name__ == "__main__":
    app.run(debug=True)