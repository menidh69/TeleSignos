import os
from datetime import datetime
from flask import render_template, session, redirect, url_for, send_from_directory
from . import main
from .forms import NameForm, MunicipioForm, ColoniaForm 
from .. import db
from ..models import *
from flask_login import login_required

@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.home'))
    return redirect(url_for('auth.login'))

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join('static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@main.route('/home')
@login_required
def home():
    return render_template('home.html')


@main.route('/tablas')
@login_required
def tablas():
    return render_template('tablas.html')


@main.route('/tablas/<tabla>')
@login_required
def show_tabla(tabla):
    return render_template('crud.html', tabla = tabla)

@main.route('/tablas/municipios/new', methods=['GET', 'POST'])
@login_required
def new_municipio():
    form = MunicipioForm()
    if form.validate_on_submit():
        municipio = Municipio(id_municipio=form.id_municipio.data, nombre_municipio=form.nombre_municipio.data)
        db.session.add(municipio)
        return redirect(url_for('.tablas.municipios.new'))
    return render_template('new.html', form = form, tabla= 'municipio')

@main.route('/tablas/colonias/new', methods=['GET', 'POST'])
@login_required
def new_colonia():
    form = ColoniaForm()
    if form.validate_on_submit():
        colonia = Colonia(id_colonia=form.id_colonia.data, nombre_colonia=form.nombre_colonia.data, id_municipio=form.id_municipio.data)
        db.session.add(colonia)
        return redirect('/tablas/colonias/new')
    return render_template('new.html', form = form, tabla= 'colonias')

@main.route('/help')
@login_required
def help():
    return render_template('help.html')