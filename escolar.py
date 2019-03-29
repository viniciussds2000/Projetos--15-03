# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *
from bdsimulado import *

# Instanciando a app Flask
app = Flask(__name__)


mysql = MySQL()
mysql.init_app(app)

#configurando acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'escolar'


# Rota para /


@app.route('/')
def principal():
    return render_template('index.html')

# Rota para /login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        cursor = mysql.get_db().cursor()

        #obter o idlogin
        idlogin = get_idlogin(cursor,login,senha)

        # Verificar a senha
        if idlogin is None:
            return render_template('index.html', erro='Login/senha incorretos!')
        else:

            return render_template('oi.html', nome=login, disciplinas=get_disciplinas(cursor,idlogin))



    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

# Rota para detalhar dsciplina
@app.route('/detalhar/<disciplina>')
def detalhar(disciplina):
    return render_template('disciplina.html', disciplina = disciplina, detalhe=get_detalhes(disciplina), detativ=get_detativ(disciplina))


# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)