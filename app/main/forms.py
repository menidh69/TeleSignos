from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField, DateTimeField, ValidationError
from wtforms.fields.html5 import DateTimeLocalField, DateField
from wtforms.validators import Required, Optional, Length, Email, Regexp, EqualTo
from ..models import Usuario


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()]) 
    submit = SubmitField('Submit')

class MunicipioForm(Form):
    id_municipio = IntegerField("id", validators=[Required()])
    nombre_municipio = StringField("Municipio:", validators=[Required()])
    submit = SubmitField('Submit')

class ColoniaForm(Form):
    id_colonia = IntegerField("id", validators=[Required()])
    nombre_colonia = StringField("Nombre Colonia:", validators=[Required()])
    id_municipio = SelectField("Municipio", choices=[], validators=[Required()])
    submit = SubmitField('Submit')

class HospitalForm(Form):
    id_municipio = SelectField("id_municipio", choices=[],validators=[Required()])
    nombre_hospital = StringField("Hospital:", validators=[Required()])
    direccion = StringField("Direccion:", validators=[Required()])
    telefono = StringField("telefono:", validators=[Required()])
    email = StringField("Email:", validators=[Required()])
    submit = SubmitField('Submit')

class ServicioForm(Form):
    servicio_nombre = StringField("Servicio:", validators=[Required()])
    contacto = StringField("Direccion:", validators=[Required()])
    telefono = StringField("telefono:", validators=[Required()])
    email = StringField("Email:", validators=[Required()])
    submit = SubmitField('Submit')

class AmbulanciaForm(Form):
    num_unidad = StringField("Numero de unidad:", validators=[Required()])
    id_servicio = SelectField("id_servicio", choices=[], validators=[Required()])
    submit = SubmitField('Submit')

class PacienteForm(Form):
    servicio_medico = StringField("servicio medico:", validators=[Required()])
    nombre_paciente = StringField("Nombre:", validators=[Required()])
    apellidos = StringField("Apellidos:", validators=[Required()])
    genero = StringField("Genero:", validators=[Required()])
    fecha_nac = DateField("Fecha de Nacimiento", validators=[Required()])
    id_colonia = SelectField("id_colonia", choices=[], validators=[Required()])
    submit = SubmitField('Submit')

class TipoUrgenciaForm(Form):
    urgencia = StringField("Urgencia:", validators=[Required()])
    descripcion = StringField("Descripcion:", validators=[Required()])
    submit = SubmitField('Submit')

class MovimientoForm(Form):
    id_paciente = SelectField("id_paciente", choices=[], validators=[Optional()])
    id_usuario = IntegerField("id_usuario", validators=[Optional()])
    id_hospital = SelectField("id_hospital", choices=[], validators=[Optional()])
    id_ambulancia = SelectField("id_ambulancia", choices=[], validators=[Optional()])
    id_tipo_urgencia = SelectField("id_tipo_urgencia", validators=[Optional()])
    fecha_inicio = DateTimeLocalField('Fecha y Hora Inicial', format='%Y-%m-%d', validators=[Optional()])
    fecha_final = DateTimeLocalField('Fecha y Hora Final', format='%Y-%m-%d', validators=[Optional()])
    presion_arterial = StringField('Presion Arterial', validators=[Optional()])
    frec_cardiaca = StringField('Frecuencia Cardiaca', validators=[Optional()])    
    frec_respiratoria = StringField('Frecuencia Respiratoria', validators=[Optional()])
    temperatura = StringField('Temperatura', validators=[Optional()])
    escala_glassglow = StringField('Escala Glassgow', validators=[Optional()])
    gravedad = SelectField("Gravedad", choices=[('BAJA'),('MEDIA'),('ALTA'),('MUY ALTA')], validators=[Optional()])
    submit = SubmitField('Submit')
    
class UsuarioForm(Form):
    
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    nombre_usuario = StringField("Username:", validators=[
        Required(),Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField("Password:", validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField("Confirmar Password:", validators=[Required()])
    id_tipo_usuario = SelectField("Tipo usuario:", choices=[], validators=[Required()])
    submit = SubmitField('Submit')

    def validate_user(self, field):
        if Usuario.query.filter_by(nombre_usuario=field.data).first():
            raise ValidationError('Nombre de usuario ya esta en uso')
