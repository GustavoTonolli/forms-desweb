from flask import Flask, render_template, request

# dunder method __name__ parametro especial
app = Flask(__name__) 

@app.route("/")
def index():
    return render_template('formulario.html') 

@app.route("/servidor", methods =['POST'])
def servidor():
    dados = request.form
    print(dados)
    return ''
    
# def index():
#     return 


