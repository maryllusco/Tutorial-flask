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
