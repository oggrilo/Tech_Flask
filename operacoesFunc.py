import mysql.connector
import conexao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserir(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc):
    try:
        sql = "insert into funcionario(codigoFunc, nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) values('','{}','{}','{}','{}','{}')".format(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, "Inserido!")
    except Exception as erro:
        print(erro)

#Consultar os dados do BD
def selecionar():
    try:
        sql = "select * from funcionario"
        con.execute(sql)

        for (nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc) in con:
            print(nomeFunc, cpfFunc, celularFunc, salarioFunc, senhaFunc)
        print('\n')
    except Exception as erro:
        print(erro)

#Atualizar dados no banco de dados
def atualizarNome(codigoFunc, nomeFunc):
    try:
        sql = "update funcionario set nomeFunc = '{}' where codigoFunc = '{}'".format(nomeFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizarCelular(codigoFunc, celularFunc):
    try:
        sql = "update funcionario set celularFunc = '{}' where codigoFunc = '{}'".format(celularFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def atualizaSalario(codigoFunc, salarioFunc):
    try:
        sql = "update funcionario set salarioFunc = '{}' where codigoFunc = '{}'".format(salarioFunc, codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualzado!")
    except Exception as erro:
        print(erro)

def atualizarSenha(codigoFunc, senhaFunc):
    try:
        sql = "update funcionario set senhaFunc = '{}' where codigoFunc = '{}'".format(senhaFunc,codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Atualizado!")
    except Exception as erro:
        print(erro)

def excluir(codigoFunc):
    try:
        sql = "delete from funcionario where codigoFunc = '{}'".format(codigoFunc)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Deletada!")
    except Exception as erro:
        print(erro)