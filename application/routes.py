from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpenses


@app.route("/")
def index():
    return render_template('index.html', title = 'index')

@app.route("/add", methods = ["GET", "POST"])
def add_expense():
    form = UserInputForm()                                              # Creates an instance of the UserInputForm, a child of flask_wtf FlaskForm
    if form.validate_on_submit():                                       # Returns true if all validators (DataRequired checks) are true
        entry = IncomeExpenses(type = form.type.data,                   # Creates an instance of IncomeExpenses representing a new row in the Income Expenses class
                               amount = form.amount.data,
                               category = form.category.data,
                               )
        db.session.add(entry)                                           # Session is temporary holding area for database changes that need to be committed
        db.session.commit()                                             # Add current session to the income_expenses table
        flash("Successful Entry", 'success')                            # flash is a flask global function that sens one-time message

        return redirect(url_for('index'))                               # If form valid, return user to index page

    return render_template("add.html", title = 'add', form = form)      # I do not understand how jinja2 is receiving this form...
