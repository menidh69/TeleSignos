import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from models import *
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField from wtforms.validators import Required



app = Flask(__name__)
Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NameForm(Form):
name = StringField('What is your name?', validators=[Required()]) 
submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('login.html', form=form, name=session.get('name'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')

@app.route('/tablas/<tabla>')
def show_tabla(tabla):
    return render_template('crud.html', tabla = tabla)

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)