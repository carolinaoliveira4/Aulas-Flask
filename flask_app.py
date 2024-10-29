
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect, make_response, abort, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
  name = StringField('What is your name?', validators= [DataRequired()])
  submit = SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Chave forte'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'))


@app.route('/user/<user>/<prontuario>/<inst>')
def identificacao(user, prontuario, inst):
    return render_template('user.html', user = user, prontuario = prontuario, inst = inst)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

@app.route('/contextorequisicao/<user>')
def contextorequisicao(user):
    user_agent = request.headers.get('User-Agent')
    return render_template('contexto.html', user = user, navegador = user_agent, ip = request.remote_addr, host = request.url)

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

