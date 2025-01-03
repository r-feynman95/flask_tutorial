from application import app
from flask import render_template
from application.form import UserInputForm

@app.route("/")
def index():
    return render_template('index.html', title = 'index')

@app.route("/add")
def add_expense():
    form = UserInputForm()
    return render_template("add.html", title = 'add', form = form)
