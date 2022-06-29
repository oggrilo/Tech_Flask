import menuADM
import menuCliente
import login
from flask import Flask, render_template, request, flash, url_for

import operacoesFunc
import operacoesLogin
import this

#var_func
this.nomeFunc = ""
this.cpfFunc = ""
this.celularFunc = ""
this.salarioFunc = ""
this.senhaFunc = ""
this.cargo = ""

this.dados = ""
this.mensagem = ""

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET', 'POST'])
def pag_inicial():
    return render_template('/index.html', titulo='Página Principal')

#cadastrar Funcionário
@pessoa.route('/cadastrarFunc.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nomeFunc = request.form['tNovoNomeFunc']
        this.cpfFunc = request.form['tNovoCpfFunc']
        this.celularFunc = request.form['tNovoCelularFunc']
        this.salarioFunc = request.form['tNovoSalarioFunc']
        this.senhaFunc = request.form['tNovoSenhaFunc']
        this.cargo = request.form['Cargo']

        if operacoesLogin.cpf_validate(this.cpfFunc) == True:
            this.dados = operacoesFunc.inserirFunc(this.nomeFunc, this.cpfFunc, this.celularFunc, this.salarioFunc, this.senhaFunc, this.cargo)
            return render_template('/cadastrarFunc.html', titulo='Página De Cadastro Dos Funcionário', resultado=this.dados)
        else:
            this.dados = "CPF não é válido, favor cadastrar com CPF existente!"
    return render_template('/cadastrarFunc.html', titulo='Página De Cadastro Dos Funcionário', resultado=this.dados)


#consultar Funcionário por nome
@pessoa.route('/consultarFunc.html', methods=['GET', 'POST'])
def consultar_por_nome():
    if request.method == 'POST':
        this.nomeFunc = request.form['tNovoNomeFunc']
        this.mensagem = operacoesFunc.selecionar_func(this.nomeFunc)
    else:
        this.mensagem = ""
    return render_template('/consultarFunc.html', titulo='Página De Consulta Dos Funcionários', dados=this.mensagem)



if __name__ == "__main__":
    pessoa.run(debug=True, port=5000)
    #login.escolhas()
    #menuADM.operacao()
    #menuCliente.operacao()