from flask import Flask 
from models import db 

#se crea una instancia de la aplicacion Flask 
app = Flask(__name__) #estamos creando la aplicacion de flask 

#configurar la URL de la bas de datos
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///clientes_fieles.db'
#Inicializamos la extension SQLALCHEMY en la app Flask 
db.init_app(app)

#con esto se asegura que las operaciones con la base de datos se realicen correctamente 
with app.app_context():
    db.create_all()


