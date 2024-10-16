
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect, make_response, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<user>')
def hello_user(user):
    return render_template('user.html', user = user)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

# @app.route('/contextorequisicao')
# def contextorequisicao():
#     user_agent = request.headers.get('User-Agent')
#     return render_template('contexto.html', navegador = user_agent, ip = request.remote_addr, host = request.url)

# @app.route('/redirecionamento')
# def redirecionamento():
#     return redirect('https://ptb.ifsp.edu.br/', code=302) # Se questionar porquê do código 302, é porque ele é o código HTTP que informa ser um redirecionamento

# @app.route('/objetoresposta')
# def cookie():
#     resposta = make_response('<h1>This document carries a cookie!</h1>')
#     resposta.set_cookie('Exemplo_cookie', "Positivo")
#     return resposta

# @app.route('/codigostatusdiferente')
# def codigo_status_diferente():
#     return 'DESCOBRIR'

# @app.route('/abortar')
# def abortar():
#     abort(404)

