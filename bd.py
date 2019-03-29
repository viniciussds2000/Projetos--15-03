#Função validar login
def get_idlogin(cursor,login,senha):
    #executar SQL
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}"')

    # recuperando o  retorno  do BD
    idlogin = cursor.fetchone()

    #Fechar o cursor
    cursor.close()

    #retornar idlogin
    return idlogin

#Funcao para retornar as disciplinas
def get_notas(cursor,idlogin):
    #executar o sql
    cursor.execute(f'select disciplina,nota1,nota2,nota3,from notas where idlogin = {idlogin}')

