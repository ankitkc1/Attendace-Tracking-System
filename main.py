from flask import Flask, render_template, url_for, request, redirect, flash
from register import SetData
from attend import attendence
import pandas as pd


app = Flask(__name__)
app.secret_key = 'my secret key'
df = pd.read_csv('attendence.csv')
df.to_csv('attendence.csv', index=False)
pas = "password"

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def home_after_registration():
    id = request.form['Student_id']
    password = request.form['password']
    if password == pas:
        SetData(id)
        flash("Registration Successful")
        return render_template("index.html")
    else:
        flash("check password")
        return render_template("index.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template("regiser.html")


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    marked = attendence()
    if(marked == True):
        flash("Attendence Marked Successfully")
    else:
        flash("You are not registered yet")

    return render_template("index.html")

@app.route('/table')
def table():
    
    data = pd.read_csv('attendence.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])


if __name__ == '__main__':
    app.run(debug = True)
