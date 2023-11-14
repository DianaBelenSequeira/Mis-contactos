from flask_sqlalchemy import SQLAlchemy 

#inicializar la extension SQLachemy 
db=SQLAlchemy()

#definimos una clase que representa una tabla en la base de datos 
class Contactos(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[20], nullable=False)
    apellido= db.Column(db.String[20], nullable=False)
    numero= db.Column(db.String[20], nullable=False)

    #Constructor de clase [20]
    def __init__(self, nombre, apellido, numero): 
        self.nombre=nombre
        self.apellido=apellido
        self.numero= numero 