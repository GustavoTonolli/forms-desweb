from flask import Flask, request

# dunder method __name__ parametro especial
app = Flask(__name__) 

@app.route("/")
def index():
    return '''
           <h1>Eu não acredito!</h1> 
           '''
@app.route("/aff")
def aff():
    return '''
           <h1>aff! É verdade mesmo!</h1> 
           '''


