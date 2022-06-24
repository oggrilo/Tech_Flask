import mysql.connector
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserir(nomeLanche, descricaoLanche, valorLanche, quantidadeLanche):
    try:
        sql = "insert into lanche(codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) values('','{}','{}','{}', '{}')".format(nomeLanche, descricaoLanche, quantidadeLanche, valorLanche)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche) in con:
            print(codigoLanche, nomeLanche, descricaoLanche, quantidadeLanche, valorLanche)
        print('\n')
    except Exception as erro:
        print(erro)

def selecionarValor():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (valorLanche) in con:
            print(valorLanche)
        print('\n')
    except Exception as erro:
        print(erro)

def selecionarQuantidade():
    try:
        sql = "select * from lanche"
        con.execute(sql)

        for (quantidadeLanche) in con:
            print(quantidadeLanche)
        print('\n')
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNome(codigoLanche, nomeLanche):
    try:
        sql = "update lanche set nomeLanche = '{}' where codigoLanche = '{}'".format(nomeLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarDescricao(codigoLanche, descricaoLanche):
    try:
        sql = "update lanche set descricaoLanche = '{}' where codigoLanche = '{}'".format(descricaoLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarValor(codigoLanche, valorLanche):
    try:
        sql = "update lanche set valorLanche = '{}' where codigoLanche = '{}'".format(valorLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarQuantidade(codigoLanche, quantidadeLanche):
    try:
        sql = "update lanche set quantidadeLanche = '{}' where codigoLanche = '{}'".format(quantidadeLanche,codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigoLanche):
    try:
        sql = "delete from lanche where codigoLanche = '{}'".format(codigoLanche)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)