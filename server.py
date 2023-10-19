from flask import Flask, render_template, request

# dunder method __name__ parametro especial
app = Flask(__name__) 

@app.route("/")
def index():
    return render_template('formulario.html') 

@app.route("/servidor", methods =['POST'])
def servidor():
    dados = request.form
    print(dados.get('nome'))
    print(dados.get('senha'))
    print(dados.get('data'))
    print(dados.get('sexo'))
    print(dados.get('chocolate'))
    print(dados.get('coca'))
    print(dados.get('arquivo'))
    meuarquivo = request.files['arquivo']
    if meuarquivo != None:
        meuarquivo.save('/Users/gustavotonolli/Documents' + meuarquivo.filename)
    return ''
    
# def index():
#     return 


