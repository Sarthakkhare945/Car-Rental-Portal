from flask import Flask,render_template,request,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import requests

app = Flask(__name__)

from sqlalchemy.sql import exists

# database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/carrental'

db = SQLAlchemy(app)

class Contdetail(db.Model):
    sno = db.Integer()
    fname = db.Column(db.Integer,primary_key = True)
    lname = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    selectcar = db.Column(db.String, nullable = False)
    message  = db.Column(db.String, nullable = False)


    def __repr__(self) -> str:
        return f'{self.sno}-{self.fname}'

class Tripdetails(db.Model):
    sno = db.Integer()
    pick_address = db.Column(db.String,primary_key=  True,nullable =True)
    drop_address =  db.Column(db.String,nullable = True)
    Journey_date =  db.Column(db.String,nullable = False)
    
    return_date =  db.Column(db.String,nullable = False)

@app.route('/',methods = ['GET','POST'])
@app.route('/index',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        pick_address = request.form['pick_address']
        drop_address = request.form['drop_address']
        Journey_date = request.form['Journey_date']
        return_date = request.form['return_date']

        entry = Tripdetails(pick_address = pick_address, drop_address = drop_address, Journey_date = Journey_date ,return_date = return_date)

        db.session.add(entry)
        db.session.commit()

        # return 'form submitted'
        return render_template('availablecars.html')    
    return render_template('index.html',index= "class=active")




@app.route('/availablecars',methods = ['GET','POST'])
def carsavailable():
 
    req = open('data.json','r').read()

    datas = json.loads(req)
    # print(datas)



    if request.method == 'POST':
        pick_address = request.form['pick_address']
        drop_address = request.form['drop_address']
        Journey_date = request.form['Journey_date']
        return_date = request.form['return_date']

        entry = Tripdetails(pick_address = pick_address, drop_address = drop_address, Journey_date = Journey_date ,return_date = return_date)

        db.session.add(entry)
        db.session.commit()

        # for available cars from my json

    return render_template('availablecars.html', datas = datas)    
    return render_template('availablecars.html')


        
@app.route('/services')
def services():
    return render_template('services.html',services="class=active")

@app.route('/cars')
def cars():
    return render_template('cars.html',cars = "class=active")



@app.route('/contact',methods = ['GET','POST'])
def Contact():
    

    # For selecting cars

    req = open('data.json','r').read()
    datas = json.loads(req)


    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        selectcar = request.form['selectcar']
        message = request.form['message']

        
    
        entry = Contdetail(fname = fname, lname = lname,email = email, message = message,selectcar = selectcar)
        entryexist = Contdetail.query.filter_by(email=email).first()
        if not entryexist:
            db.session.add(entry)
            db.session.commit()
            db.session.remove()

        elif entryexist:
            emailexist = 'Email Already exists'
            
            return render_template('contact.html',datas = datas,emailexist=emailexist)




        else:
    
            return render_template('contact.html',contact = "class=active",datas = datas)
    return render_template('contact.html',contact = "class=active",datas = datas)
        



@app.route('/about')
def about():
    return render_template('about.html',about = "class=active")



@app.route('/tryflaskjson')
def tryflaskjson():
    import json
    f = open('data.json','r').read()
    datas = json.loads(f)
    return render_template('tryjsonflask.html',datas = datas)
    






if __name__ == '__main__':
    app.run(debug = True)

