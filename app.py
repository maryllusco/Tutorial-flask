from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
      <a href='/hola'>hola</a>
      <a href='/chau'>chau</a 
      """

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
