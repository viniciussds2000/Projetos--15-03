# Importando bibliotecas
from flask import Flask, request, render_template
from bdsimulado import *

# Instanciando a app Flask
app = Flask(__name__)

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

        # Verificar a senha
        if validar_login(login, senha):
            return render_template('oi.html', nome=login, disciplinas=get_disciplinas(login))
        else:
            return render_template('index.html', erro='Login/senha incorretos!')

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

# Rota para detalhar dsciplina
@app.route('/detalhar/<disciplina>')
def detalhar(disciplina):
    return render_template('disciplina.html', disciplina = disciplina, detalhe=get_detalhes(disciplina), detativ=get_detativ(disciplina))

def detatividade(deta):
    return render_template()

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)