from flask import Flask, render_template, redirect, url_for, flash
from flask.globals import request
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy

#création de l'objet de classe Flask
app = Flask(__name__)

#définition de route 
#@app.route('/')
#def hello_world():
# return 'hello world voici mon premier projet flask'

#configuration de la connection a la base de donnee
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/gestionemployees'
app.config['SECRET_KEY'] = "secret key"  
   
db = SQLAlchemy(app)  

class Employees(db.Model):
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
    

    
    @app.route('/add', methods =['GET', 'POST'])
    
    def addEmployee():
       if request.method == 'POST':
           if not request.form['nom']  or not request.form['prenom'] or not request.form['salaire'] or not request.form['age'] or not request.form['matricule']:
            flash("Veuillez remplir les champs s'il vous plait")
           else:
               employee =Employees(request.form['nom'], request.form['prenom'], request.form['salaire'], request.form['age'], request.form['matricule'])
               
               db.session.add(employee)
               db.session.commit()
               flash('Record was successfully added')  
               return render_template('list_employees')
           
    @app.route('/liste/', methods =['GET'])  
    def list_employees():  
     return render_template('list_employees.html', Employees = Employees.query.all())  
        
              
            
    if __name__ == '__main__':  
             db.create_all()  
             app.run(debug = True)  