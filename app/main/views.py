import os
from datetime import datetime
from flask import render_template, session, redirect, url_for, send_from_directory
from . import main
from .forms import NameForm, MunicipioForm, UsuarioForm, ColoniaForm, HospitalForm, ServicioForm, AmbulanciaForm, PacienteForm, TipoUrgenciaForm, MovimientoForm 
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


# GET & POST NEW REGISTRO
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

@main.route('/tablas/hospitales/new', methods=['GET', 'POST'])
@login_required
def new_hospital():
    form = HospitalForm()
    if form.validate_on_submit():
        hospital = Hospital(id_hospital=form.id_hospital.data, id_municipio=form.id_municipio.data, nombre_hospital=form.nombre_hospital.data, direccion=form.direccion.data, telefono=form.telefono.data, email=form.email.data)
        db.session.add(hospital)
        return redirect('/tablas/hospitales/new')
    return render_template('new.html', form = form, tabla= 'hospitales')


@main.route('/tablas/servicios/new', methods=['GET', 'POST'])
@login_required
def new_servicio():
    form = ServicioForm()
    if form.validate_on_submit():
        servicio = Servicio(id_servicio=form.id_servicio.data, servicio_nombre=form.servicio_nombre.data, contacto=form.contacto.data, telefono=form.telefono.data, email=form.email.data)
        db.session.add(servicio)
        return redirect('/tablas/servicios/new')
    return render_template('new.html', form = form, tabla= 'servicios')


@main.route('/tablas/ambulancias/new', methods=['GET', 'POST'])
@login_required
def new_ambulancia():
    form = AmbulanciaForm()
    if form.validate_on_submit():
        ambulancia = Ambulancia(id_ambulancia=form.id_ambulancia.data, num_unidad=form.num_unidad.data, id_servicio=form.id_servicio.data)
        db.session.add(ambulancia)
        return redirect('/tablas/ambulancias/new')
    return render_template('new.html', form = form, tabla= 'ambulancias')

@main.route('/tablas/usuarios/new', methods=['GET', 'POST'])
@login_required
def new_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(id_usuario=form.id_usuario.data, id_tipo_usuario=form.id_tipo_usuario.data, nombre_usuario=form.nombre_usuario.data, password_hash=form.password_hash.data)
        db.session.add(usuario)
        return redirect('/tablas/usuarios/new')
    return render_template('new.html', form = form, tabla= 'usuarios')

@main.route('/tablas/pacientes/new', methods=['GET', 'POST'])
@login_required
def new_paciente():
    form = PacienteForm()
    if form.validate_on_submit():
        paciente = Paciente(id_paciente=form.id_paciente.data, nombre_paciente=form.nombre_paciente.data, apellidos=form.apellidos.data, genero=form.genero.data, fecha_nac=form.fecha_nac.data, id_colonia=form.id_colonia.data)
        db.session.add(paciente)
        return redirect('/tablas/pacientes/new')
    return render_template('new.html', form = form, tabla= 'pacientes')

@main.route('/tablas/tipo_urgencia/new', methods=['GET', 'POST'])
@login_required
def new_tipo_urgencia():
    form = TipoUrgenciaForm()
    if form.validate_on_submit():
        tipo = Tipo_Urgencia(id_tipo_urgencia=form.id_tipo_urgencia.data, urgencia=form.urgencia.data, descripcion=form.descripcion.data)
        db.session.add(tipo)
        return redirect('/tablas/tipo_urgencia/new')
    return render_template('new.html', form = form, tabla= 'tipo_urgencia')

@main.route('/tablas/movimientos/new', methods=['GET', 'POST'])
@login_required
def new_movimiento():
    form = MovimientoForm()
    if form.validate_on_submit():
        movimiento = Movimiento(id_movimiento=form.id_movimiento.data, 
        id_paciente=form.id_paciente.data, id_usuario=form.id_usuario.data, 
        id_hospital=form.id_hospital.data, id_ambulancia=form.id_ambulancia.data, 
        id_tipo_urgencia=form.id_tipo_urgencia.data, fecha_inicio=form.fecha_inicio.data,
        fecha_final=form.fecha_final.data, presion_arterial=form.presion_arterial.data, 
        frec_cardiaca=form.frec_cardiaca.data, frec_respiratoria=form.frec_respiratoria.data, 
        temperatura=form.temperatura.data, escala_glassgow=form.escala_glassglow.data, gravedad=form.gravedad.data)
        db.session.add(movimiento)
        return redirect('/tablas/movimientos/new')
    return render_template('new.html', form = form, tabla= 'movimientos')

@main.route('/help')
@login_required
def help():
    return render_template('help.html')