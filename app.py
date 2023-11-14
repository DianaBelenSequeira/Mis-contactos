from flask import render_template, request, redirect, url_for
from conexion import app, db 
from models import Contactos

@app.route('/')
def index():
    return render_template('cargar_contactos.html')

#CRUD 
@app.route('/cargar_contactos', methods=['POST', 'GET'])
def cargar_contactos():
    if request.method=='POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        numero= request.form['numero']

        #creamos un objeto de la clase alumnos 
        datos_contactos = Contactos(nombre, apellido, numero)

        db.session.add(datos_contactos)
        db.session.commit()

        return render_template('cargar_contactos.html')

    return render_template('cargar_contactos.html')

@app.route('/mostrar_contactos', methods=['GET', 'POST'])
def mostrar_contactos():

    #creamos u nuevo objeto y realizamos la consulta para obtener todos los registros 
    lista_contactos = Contactos.query.all()

    return render_template('mostrar_contactos.html', lista_contactos = lista_contactos)

@app.route('/actualizar/<int:contacto_id>', methods=['GET', 'POST'])
def actualizar(contacto_id):

    contacto_a_actualizar = Contactos.query.get(contacto_id)

    if request.method=='POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        numero= request.form['numero']

        contacto_a_actualizar.nombre=nombre
        contacto_a_actualizar.apellido=apellido
        contacto_a_actualizar.numero=numero

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    return render_template('actualizar.html', contacto_a_actualizar=contacto_a_actualizar)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method=='POST':

        id=request.form['contacto_id']
        print(id)

        contacto_a_eliminar= Contactos.query.filter_by(id=id).first
        db.session.delete(contacto_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_contactos'))



if __name__ == ('__main__'):
    app.run(debug=True, port=8000)