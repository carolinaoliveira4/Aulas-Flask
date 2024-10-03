
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect, make_response, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/', code=302) # Se questionar porquê do código 302, é porque ele é o código HTTP que informa ser um redirecionamento

@app.route('/objetoresposta')
def cookie():
    resposta = make_response('<h1>This document carries a cookie!</h1>')
    resposta.set_cookie('Exemplo_cookie', "Positivo")
    return resposta

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return 'DESCOBRIR'

@app.route('/abortar')
def abortar():
    abort(404)

