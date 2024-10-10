
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect, make_response, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>/<prontuario>/<inst>')
def user(name, prontuario, inst):
    return render_template('identificacao.html', aluno = name, prontuario = prontuario, inst = inst)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    return render_template('contexto.html', navegador = user_agent, ip = request.remote_addr, host = request.url)

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

