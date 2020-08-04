from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm 
from .. import db
from ..models import *


@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('login.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())

@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/tablas')
def tablas():
    return render_template('tablas.html')

@main.route('/tablas/<tabla>')
def show_tabla(tabla):
    return render_template('crud.html', tabla = tabla)

@main.route('/help')
def help():
    return render_template('help.html')