from flask import Flask, render_template, redirect, url_for, flash
from flask import request
# from flask.globals import request
#from flask.helpers import flash 
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL



#création de l'objet de classe Flask
app = Flask(__name__)
#définition de route 
@app.route('/')
def hello_world():
 return "hello world voici mon premier projet flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:root://''@localhost/gestionemployees'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''127.0.0.1/gestionemployees'  
app.config['SECRET_KEY'] = "secret key"  
db = SQLAlchemy(app)  

class Employees(db.Model):
    __tablename__ ='employees'
    id = db.Column('employee_id', db.Integer, primary_key =True)
    nom = db.Column(db.Text(100))
    prenom = db.Column(db.Text(100))
    salaire = db.Column(db.Integer)
    age = db.Column(db.Text(200))
    matricule = db.Column(db.Text(10))
    
# création d'une fonction  
def __init__ (self, prenom, nom, salaire, age, matricule):
    # self est une instance d'une classe
    self.nom= nom          
    self.prenom = prenom
    self.salaire = salaire
    self.age = age
    self.matricule = matricule
    
''' @app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['nom'] != 'nom' or request.form['prenom'] != 'prenom' or request.form['salaire'] != 'salaire' or request.form['age'] != 'age' or request.form['matricule'] != 'matricule':
            error = 'Invalid . Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('log.html', error=error)
 '''

@app.route('/add', methods = ['GET', 'POST'])
def addEmployees():
    return render_template('add.html')

''' if request.method == 'POST':
     nom = request.form['nom']
     prenom = request.form['prenom']
     salaire = request.form['salaire']
     age = request.form['age']
     matricule = request.form['matricule']
   return render_template('add.html')
  '''


''' if request.method == 'POST': 
    if not request.form['nom'] or not request.form['prenom'] or not request.form['salaire'] or not request.form['age'] or not request.form['matricule']:
    
        flash("Veuillez remplir les champs s'il vous plait")
    else:                                                                                                                                                              
     employee = Employees(request.form['nom'] and request.form['prenom'] and request.form['salaire'] and 
            request.form['age'] and request.form['matricule'])  
     db.session.add(employee)  
     db.session.commit()  
   
   
   
    if __name__ == '__main__':  
     db.create_all()  
    app.run(debug = True)    '''