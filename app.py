from flask import Flask, url_for 
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

db=None
def abrirConexion():
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = sqlite3.Row
    return db


def cerrarConexion():
    global db
    db=abrirConexion()
    db=None
@app.route("/usuarios/")
def obterGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    cerrarConexion()
    fila = [dict(row) for row in resultado]
    return str(fila)




