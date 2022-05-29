#required imports for application
from flask import Flask, render_template, request, flash
from register import SetData
from attend import attendence
import pandas as pd


#iniialization
app = Flask(__name__)
df = pd.read_csv('attendence.csv')
df.to_csv('attendence.csv', index=False)
pas = "password"

#for home page
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
        flash("wrong password")
        return render_template("index.html")

#for registration page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template("regiser.html")


#for marking attendence
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    marked = attendence()
    if(marked == True):
        flash("Attendence Marked Successfully")
    else:
        flash("You are not registered yet")
    
    return render_template("index.html")


#for table page
@app.route('/table')
def table():
    
    data = pd.read_csv('attendence.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])

#running the application
if __name__ == '__main__':
    app.run(debug = True)
