import menuADM
import menuCliente
import login
from flask import Flask, render_template, request
import operacoesFunc

import this

this.nomeFunc = ""
this.cpfFunc = ""
this.celularFunc = ""
this.salarioFunc = ""
this.senhaFunc = ""
this.cargo = ""
this.dados = ""

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nomeFunc = request.form['tNovoNomeFunc']
        this.cpfFunc = request.form['tNovoCpfFunc']
        this.celularFunc = request.form['tNovoCelularFunc']
        this.salarioFunc = request.form['tNovoSalarioFunc']
        this.senhaFunc = request.form['tNovoSenhaFunc']
        this.cargo = request.form['inputCargo']
        this.dados = operacoesFunc.inserir(this.nomeFunc, this.cpfFunc, this.celularFunc, this.salarioFunc, this.senhaFunc)
    return render_template('index.html', titulo='Página de Cadastro Funcionário', resultado=this.dados)

if __name__ == "__main__":
    pessoa.run(debug=True, port=5000)
    #login.escolhas()
    #menuADM.operacao()
    #menuCliente.operacao()