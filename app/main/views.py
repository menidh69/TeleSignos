import os
from datetime import datetime
from flask import render_template, session, redirect, url_for, send_from_directory
from . import main
from .forms import NameForm 
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


@main.route('/help')
@login_required
def help():
    return render_template('help.html')