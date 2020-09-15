from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, DateField, SelectField, DateTimeField
from wtforms.validators import Required


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
    id_paciente = SelectField("id_paciente", choices=[], validators=[Required()])
    id_usuario = IntegerField("id_usuario", validators=[Required()])
    id_hospital = SelectField("id_hospital", choices=[], validators=[Required()])
    id_ambulancia = SelectField("id_ambulancia", choices=[], validators=[Required()])
    id_tipo_urgencia = SelectField("id_tipo_urgencia", choices=[], validators=[Required()])
    fecha_inicio = DateField('Fecha y Hora Inicial', validators=[Required()])
    fecha_final = DateField('Fecha y Hora Final', validators=[Required()])
    presion_arterial = StringField('Presion Arterial', validators=[Required()])
    frec_cardiaca = StringField('Frecuencia Cardiaca', validators=[Required()])    
    frec_respiratoria = StringField('Frecuencia Respiratoria', validators=[Required()])
    temperatura = StringField('Temperatura', validators=[Required()])
    escala_glassglow = StringField('Escala Glassgow', validators=[Required()])
    gravedad = SelectField("Gravedad", choices=[('BAJA'),('MEDIA'),('ALTA'),('MUY ALTA')])
    submit = SubmitField('Submit')
    
class UsuarioForm(Form):
    id_tipo_usuario = SelectField("Tipo usuario:", choices=[], validators=[Required()])
    nombre_usuario = StringField("Username:", validators=[Required()])
    password_hash = PasswordField("Password:", validators=[Required()])
    submit = SubmitField('Submit')
