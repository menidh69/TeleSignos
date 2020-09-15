import os
from datetime import datetime
from flask import render_template, session, redirect, url_for, send_from_directory
from . import main
from .forms import NameForm, MunicipioForm, UsuarioForm, ColoniaForm, HospitalForm, ServicioForm, AmbulanciaForm, PacienteForm, TipoUrgenciaForm, MovimientoForm 
from .. import db
from ..models import * 
from flask_login import login_required, current_user
from .. import models as models

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join('static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@main.route('/')
@login_required
def index():
    return render_template('home.html')


@main.route('/catalogo')
@login_required
def tablas():
    return render_template('tablas.html')


@main.route('/catalogo/<table>')
@login_required
def show_table(table):
    TableDict = {"municipios":"Municipio", "colonias":"Colonia", "hospitales":"Hospital", "ambulancias":"Ambulancia",
    "tipo_urgencia":"Tipo_Urgencia", "movimientos":"Movimiento", "pacientes":"Paciente", "servicios": "Servicio", "usuarios":"Usuario", "bitacora":"Bitacora"}
    tableclass = getattr(models, TableDict[table])
    columns = tableclass.__table__.columns.keys()
    items = tableclass.query.all()
    return render_template('crud.html', table=table, items = items, columns = columns)


# GET & POST NEW REGISTRO
@main.route('/catalogo/municipios/new', methods=['GET', 'POST'])
@login_required
def new_municipio():
    form = MunicipioForm()
    if form.validate_on_submit():
        municipio = Municipio(id_municipio=form.id_municipio.data, nombre_municipio=form.nombre_municipio.data)
        db.session.add(municipio)
        return redirect(url_for('.tablas.municipios.new'))
    return render_template('new.html', form = form, tabla= 'municipio')

@main.route('/catalogo/colonias/new', methods=['GET', 'POST'])
@login_required
def new_colonia():
    form = ColoniaForm()
    form.id_municipio.choices = [(municipio.id_municipio, municipio.nombre_municipio) for municipio in Municipio.query.all()]
    if form.validate_on_submit():
        colonia = Colonia(id_colonia=form.id_colonia.data, nombre_colonia=form.nombre_colonia.data, id_municipio=form.id_municipio.data)
        db.session.add(colonia)
        return redirect('/catalogo/colonias/new')
    return render_template('new.html', form = form, tabla= 'colonias')

@main.route('/catalogo/hospitales/new', methods=['GET', 'POST'])
@login_required
def new_hospital():
    form = HospitalForm()
    form.id_municipio.choices = [(municipio.id_municipio, municipio.nombre_municipio) for municipio in Municipio.query.all()]
    if form.validate_on_submit():
        hospital = Hospital(id_municipio=form.id_municipio.data, nombre_hospital=form.nombre_hospital.data, direccion=form.direccion.data, telefono=form.telefono.data, email=form.email.data)
        db.session.add(hospital)
        return redirect('/catalogo/hospitales/new')
    return render_template('new.html', form = form, tabla= 'hospitales')


@main.route('/catalogo/servicios/new', methods=['GET', 'POST'])
@login_required
def new_servicio():
    form = ServicioForm()
    if form.validate_on_submit():
        servicio = Servicio(servicio_nombre=form.servicio_nombre.data, contacto=form.contacto.data, telefono=form.telefono.data, email=form.email.data)
        db.session.add(servicio)
        return redirect('/catalogo/servicios/new')
    return render_template('new.html', form = form, tabla= 'servicios')


@main.route('/catalogo/ambulancias/new', methods=['GET', 'POST'])
@login_required
def new_ambulancia():
    form = AmbulanciaForm()
    form.id_servicio.choices = [(servicio.id_servicio, servicio.servicio_nombre) for servicio in Servicio.query.all()]
    if form.validate_on_submit():
        ambulancia = Ambulancia(num_unidad=form.num_unidad.data, id_servicio=form.id_servicio.data)
        db.session.add(ambulancia)
        return redirect('/catalogo/ambulancias/new')
    return render_template('new.html', form = form, tabla= 'ambulancias')

@main.route('/catalogo/usuarios/new', methods=['GET', 'POST'])
@login_required
def new_usuario():
    form = UsuarioForm()
    form.id_tipo_usuario.choices = [(tipo.id_tipo_usuario, tipo.tipo_usuario) for tipo in Tipo_Usuario.query.all()]
    if form.validate_on_submit():
        usuario = Usuario(id_tipo_usuario=form.id_tipo_usuario.data, nombre_usuario=form.nombre_usuario.data, password_hash=form.password_hash.data)
        db.session.add(usuario)
        return redirect('/catalogo/usuarios/new')
    return render_template('new.html', form = form, tabla= 'usuarios')

@main.route('/catalogo/pacientes/new', methods=['GET', 'POST'])
@login_required
def new_paciente():
    form = PacienteForm()
    form.id_colonia.choices = [(colonia.id_colonia, colonia.nombre_colonia) for colonia in Colonia.query.all()]
    if form.validate_on_submit():
        paciente = Paciente(servicio_medico=form.servicio_medico.data, nombre_paciente=form.nombre_paciente.data, apellidos=form.apellidos.data, genero=form.genero.data, fecha_nac=form.fecha_nac.data, id_colonia=form.id_colonia.data)
        db.session.add(paciente)
        return redirect('/catalogo/pacientes/new')
    return render_template('new.html', form = form, tabla= 'pacientes')

@main.route('/catalogo/tipo_urgencia/new', methods=['GET', 'POST'])
@login_required
def new_tipo_urgencia():
    form = TipoUrgenciaForm()
    if form.validate_on_submit():
        tipo = Tipo_Urgencia(urgencia=form.urgencia.data, descripcion=form.descripcion.data)
        db.session.add(tipo)
        return redirect('/catalogo/tipo_urgencia/new')
    return render_template('new.html', form = form, tabla= 'tipo_urgencia')

@main.route('/catalogo/movimientos/new', methods=['GET', 'POST'])
@login_required
def new_movimiento():
    form = MovimientoForm()
    form.id_paciente.choices = [(paciente.id_paciente, paciente.apellidos) for paciente in Paciente.query.all()]
    form.id_hospital.choices = [(hospital.id_hospital, hospital.nombre_hospital) for hospital in Hospital.query.all()]
    form.id_ambulancia.choices = [(ambulancia.id_ambulancia, ambulancia.num_unidad) for ambulancia in Ambulancia.query.all()]
    form.id_tipo_urgencia.choices = [(tipo.id_tipo_urgencia, tipo.urgencia) for tipo in Tipo_Urgencia.query.all()]
    form.id_usuario = current_user.id_usuario
    if form.validate_on_submit():
        movimiento = Movimiento(
        id_paciente=form.id_paciente.data, id_usuario=current_user.id_usuario, 
        id_hospital=form.id_hospital.data, id_ambulancia=form.id_ambulancia.data, 
        id_tipo_urgencia=form.id_tipo_urgencia.data, fecha_inicio=form.fecha_inicio.data,
        fecha_final=form.fecha_final.data, presion_arterial=form.presion_arterial.data, 
        frec_cardiaca=form.frec_cardiaca.data, frec_respiratoria=form.frec_respiratoria.data, 
        temperatura=form.temperatura.data, escala_glassgow=form.escala_glassglow.data, gravedad=form.gravedad.data)
        db.session.add(movimiento)
        return redirect('/catalogo/movimientos')
    return render_template('new.html', form = form, tabla= 'movimientos')

@main.route('/catalogo/municipios/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_municipio(id):
    municipio = Municipio.query.get_or_404(id)
    form = MunicipioForm()
    if form.validate_on_submit():
        municipio.id_municipio = form.id_municipio.data
        municipio.nombre_municipio = form.nombre_municipio.data
        db.session.add(municipio)
        return redirect('/catalogo/municipios')
    form.id_municipio.data = municipio.id_municipio
    form.nombre_municipio.data = municipio.nombre_municipio
    return render_template('edit.html', form=form)

@main.route('/catalogo/municipios/delete/<int:id>', methods=['POST'])
@login_required
def del_municipio(id):
    municipio = Municipio.query.get_or_404(id)
    db.session.delete(municipio)
    db.session.commit()
    return redirect("/catalogo/municipios")

@main.route('/catalogo/colonias/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_colonia(id):
    colonia = Colonia.query.get_or_404(id)
    form = ColoniaForm()
    form.id_municipio.choices = [(municipio.id_municipio, municipio.nombre_municipio) for municipio in Municipio.query.all()]
    if form.validate_on_submit():
        colonia.id_colonia = form.id_colonia.data
        colonia.id_municipio = form.id_municipio.data
        colonia.nombre_colonia = form.nombre_colonia.data
        db.session.add(colonia)
        return redirect('/catalogo/colonias')
    form.id_colonia.data = colonia.id_colonia
    form.id_municipio.data = colonia.id_municipio 
    form.nombre_colonia.data=colonia.nombre_colonia
    return render_template('edit.html', form=form)
    
@main.route('/catalogo/colonias/delete/<int:id>', methods=['GET'])
@login_required
def del_colonia(id):
    colonia = Colonia.query.get_or_404(id)
    db.session.delete(colonia)
    db.session.commit()
    return redirect("/catalogo/colonias")

@main.route('/catalogo/hospitales/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_hospital(id):
    hospital = Hospital.query.get_or_404(id)
    form = HospitalForm()
    form.id_municipio.choices = [(municipio.id_municipio, municipio.nombre_municipio) for municipio in Municipio.query.all()]
    if form.validate_on_submit():
        hospital.id_municipio=form.id_municipio.data
        hospital.nombre_hospital=form.nombre_hospital.data
        hospital.direccion=form.direccion.data
        hospital.telefono=form.telefono.data
        hospital.email=form.email.data
        db.session.add(hospital)
        return redirect('/catalogo/hospitales')
    form.id_municipio.data=hospital.id_municipio
    form.nombre_hospital.data=hospital.nombre_hospital
    form.direccion.data=hospital.direccion
    form.telefono.data=hospital.telefono
    form.email.data=hospital.email
    return render_template('edit.html', form=form)
    
@main.route('/catalogo/hospitales/delete/<int:id>', methods=['GET'])
@login_required
def del_hospital(id):
    hospital = Hospital.query.get_or_404(id)
    db.session.delete(hospital)
    db.session.commit()
    return redirect("/catalogo/hospitales")

@main.route('/catalogo/ambulancias/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_ambulancia(id):
    ambulancia = Ambulancia.query.get_or_404(id)
    form = AmbulanciaForm()
    form.id_servicio.choices = [(servicio.id_servicio, servicio.servicio_nombre) for servicio in Servicio.query.all()]
    if form.validate_on_submit():
        ambulancia.num_unidad=form.num_unidad.data
        ambulancia.id_servicio=form.id_servicio.data
        db.session.add(ambulancia)
        return redirect('/catalogo/ambulancias')
    form.num_unidad.data=ambulancia.num_unidad
    form.id_servicio.data=ambulancia.id_servicio
    return render_template('edit.html', form=form)
    
@main.route('/catalogo/ambulancias/delete/<int:id>', methods=['GET'])
@login_required
def del_ambulancia(id):
    ambulancia = Ambulancia.query.get_or_404(id)
    db.session.delete(ambulancia)
    db.session.commit()
    return redirect("/catalogo/ambulancias")

@main.route('/catalogo/servicios/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    form = ServicioForm()
    if form.validate_on_submit():
        servicio.servicio_nombre=form.servicio_nombre.data
        servicio.contacto=form.contacto.data
        servicio.telefono=form.telefono.data
        servicio.email=form.email.data
        db.session.add(servicio)
        return redirect('/catalogo/servicios')
    form.servicio_nombre.data=servicio.servicio_nombre
    form.contacto.data=servicio.contacto
    form.telefono.data=servicio.telefono
    form.email.data=servicio.email
    return render_template('edit.html', form=form)

@main.route('/catalogo/servicios/delete/<int:id>', methods=['GET'])
@login_required
def del_servicio(id):
    servicio = Servicio.query.get_or_404(id)
    db.session.delete(servicio)
    db.session.commit()
    return redirect("/catalogo/servicios")

@main.route('/catalogo/tipo_urgencia/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_urgencia(id):
    urgencia = Tipo_Urgencia.query.get_or_404(id)
    form = TipoUrgenciaForm()
    if form.validate_on_submit():
        urgencia.urgencia=form.urgencia.data
        urgencia.descripcion=form.descripcion.data
        db.session.add(urgencia)
        return redirect('/catalogo/tipo_urgencia')
    form.urgencia.data=urgencia.urgencia
    form.descripcion.data=urgencia.descripcion
    return render_template('edit.html', form=form)

@main.route('/catalogo/tipo_urgencia/delete/<int:id>', methods=['GET'])
@login_required
def del_urgencia(id):
    urgencia = Tipo_Urgencia.query.get_or_404(id)
    db.session.delete(urgencia)
    db.session.commit()
    return redirect("/catalogo/tipo_urgencia")


@main.route('/catalogo/pacientes/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    form = PacienteForm()
    form.id_colonia.choices = [(colonia.id_colonia, colonia.nombre_colonia) for colonia in Colonia.query.all()]
    if form.validate_on_submit():
        paciente.servicio_medico=form.servicio_medico.data
        paciente.nombre_paciente=form.nombre_paciente.data
        paciente.apellidos=form.apellidos.data
        paciente.genero=form.genero.data
        paciente.fecha_nac=form.fecha_nac.data
        paciente.id_colonia=form.id_colonia.data
        db.session.add(paciente)
        return redirect('/catalogo/pacientes')
    form.servicio_medico.data=paciente.servicio_medico
    form.nombre_paciente.data=paciente.nombre_paciente
    form.apellidos.data=paciente.apellidos
    form.genero.data=paciente.genero
    form.fecha_nac.data=paciente.fecha_nac
    form.id_colonia.data=paciente.id_colonia
    return render_template('edit.html', form=form)
    
@main.route('/catalogo/pacientes/delete/<int:id>', methods=['GET'])
@login_required
def del_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect("/catalogo/pacientes")

@main.route('/catalogo/movimientos/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_movimiento(id):
    movimiento = Movimiento.query.get_or_404(id)
    form = MovimientoForm()
    form.id_paciente.choices = [(paciente.id_paciente, paciente.apellidos) for paciente in Paciente.query.all()]
    form.id_hospital.choices = [(hospital.id_hospital, hospital.nombre_hospital) for hospital in Hospital.query.all()]
    form.id_ambulancia.choices = [(ambulancia.id_ambulancia, ambulancia.num_unidad) for ambulancia in Ambulancia.query.all()]
    form.id_tipo_urgencia.choices = [(tipo.id_tipo_urgencia, tipo.urgencia) for tipo in Tipo_Urgencia.query.all()]
    form.id_usuario = current_user.id_usuario    
    if form.validate_on_submit():
        movimiento.id_paciente=form.id_paciente.data
        movimiento.id_usuario=current_user.id_usuario
        movimiento.id_hospital=form.id_hospital.data
        movimiento.id_ambulancia=form.id_ambulancia.data
        movimiento.id_tipo_urgencia=form.id_tipo_urgencia.data
        movimiento.fecha_inicio=form.fecha_inicio.data
        movimiento.fecha_final=form.fecha_final.data
        movimiento.presion_arterial=form.presion_arterial.data
        movimiento.frec_cardiaca=form.frec_cardiaca.data
        movimiento.frec_respiratoria=form.frec_respiratoria.data
        movimiento.temperatura=form.temperatura.data
        movimiento.escala_glassgow=form.escala_glassglow.data
        movimiento.gravedad=form.gravedad.data
        db.session.add(movimiento)
        return redirect('/catalogo/movimientos')
    form.id_paciente.data=movimiento.id_paciente
    current_user.id_usuario=movimiento.id_usuario
    form.id_hospital.data=movimiento.id_hospital
    form.id_ambulancia.data=movimiento.id_ambulancia
    form.id_tipo_urgencia.data=movimiento.id_tipo_urgencia
    form.fecha_inicio.data=movimiento.fecha_inicio
    form.fecha_final.data=movimiento.fecha_final
    form.presion_arterial.data=movimiento.presion_arterial
    form.frec_cardiaca.data=movimiento.frec_cardiaca
    form.frec_respiratoria.data=movimiento.frec_respiratoria
    form.temperatura.data=movimiento.temperatura
    form.escala_glassglow.data=movimiento.escala_glassgow
    form.gravedad.data=movimiento.gravedad
    return render_template('edit.html', form=form)
    
@main.route('/catalogo/movimientos/delete/<int:id>', methods=['GET'])
@login_required
def del_movimiento(id):
    movimiento = Movimiento.query.get_or_404(id)
    db.session.delete(movimiento)
    db.session.commit()
    return redirect("/catalogo/movimientos")


@main.route('/help')
@login_required
def help():
    return render_template('help.html')