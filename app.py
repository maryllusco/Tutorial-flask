from flask import Flask, url_for, render_template
import sqlite3

app = Flask(__name__)


@app.route("/hola")
def saludar():
    return "<h2>Hello, World!</h2>"

@app.route("/chau")
def despedir():
    return "<h2>Chau!</h2>"

@app.route("/sumar/<int:n1>/<int:n2>")
def suma(n1, n2):
    suma = n1+n2
    return F"<h2>{n1} más {n2} es igual a {suma}</h2>"

@app.route("/tirar-dado/<int:caras>")
def dado (caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, salio {n}</p>"

@app.route ("/")

def main():
    url_hola = url_for("saludar")
    url_dado = url_for("dado",caras=6)
    url_logo = url_for("static",filename="logo.png")

    return f"""
    <a href= "{url_hola}">Hola</a>
    <br>
    <a href= "{url_for("despedir")}">Chau</a>
    <br>
    <a href= "{url_logo}">Logo</a>
    <br>
    <a href= "{url_dado}">Tirar_dado</a>
    """

db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None

@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"

#ruta para borrar un id 
@app.route("/borrar/<int:id>")
def borrar (id):
   abrirConexion()
   db.execute("DELETE FROM usuarios WHERE id=2" , (usr,))
   db.commit()
   cerrarConexion()

#ruta para insertar un usuario y email
@app.route("/insertar/<string:usuario>/<string:email>")
def insertar (usuario,email):
   abrirConexion()
   db.execute("INSERT INTO usuarios (usuario,email) VALUES (?, ?);", (usuario,email))
   db.commit()
   cerrarConexion()

#ruta para mostrar nombre,email del usuario
@app.route("/mostrar/<int:id>")
def mostrar(id):
   abrirConexion() #abre la conexion con la base de datos 
   cursor = db.cursor()
   cursor.execute("SELECT usuario, email FROM usuarios WHERE id=?", (id,))
   res = cursor.fetchone() #res es una variable, obtiene el resultado de la consulta                 
   cerrarConexion() #cierra la conexion con la base de datos
   return f"nombre: {res['usuario']}, email del usuario: {res['email']}"


@app.route("/mostrar-datos-plantillas/<int:id>")
def datos_plantilla(id):
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT id,usuario,email,telefono,direccion FROM usuarios WHERE id = ?;", (id,))
   res = cursor.fetchone()
   cerrarConexion()
   usuario = None
   email = None
   telefono = None
   direccion = None
   if res != None:
      usuario=res['usuario']
      email=res['email']
      telefono= res['telefono']
      direccion=res['direccion']
   return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)


 @app.route(/"lista/<int:id>")
 def lista_usuarios(id):
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario, id FROM usuarios")
   res = cursor.fetchall()
   cerrarConexion() 
   return render_template("datos2.html", usuarios=res)


