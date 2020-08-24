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
    nombre_colonia = StringField("Colonia:", validators=[Required()])
    id_municipio = IntegerField("id_municipio", validators=[Required()])
    submit = SubmitField('Submit')

class HospitalForm(Form):
    id_hospital = IntegerField("id", validators=[Required()])
    id_municipio = IntegerField("id_municipio", validators=[Required()])
    nombre_hospital = StringField("Hospital:", validators=[Required()])
    direccion = StringField("Direccion:", validators=[Required()])
    telefono = StringField("telefono:", validators=[Required()])
    email = StringField("Email:", validators=[Required()])
    submit = SubmitField('Submit')

class ServicioForm(Form):
    id_servicio = IntegerField("id", validators=[Required()])
    servicio_nombre = StringField("Servicio:", validators=[Required()])
    contacto = StringField("Direccion:", validators=[Required()])
    telefono = StringField("telefono:", validators=[Required()])
    email = StringField("Email:", validators=[Required()])
    submit = SubmitField('Submit')

class AmbulanciaForm(Form):
    id_ambulancia = IntegerField("id", validators=[Required()])
    num_unidad = StringField("Numero de unidad:", validators=[Required()])
    id_servicio = IntegerField("id_servicio", validators=[Required()])
    submit = SubmitField('Submit')

class PacienteForm(Form):
    id_paciente = IntegerField("id", validators=[Required()])
    servicio_medico = StringField("servicio medico:", validators=[Required()])
    nombre_paciente = StringField("Nombre:", validators=[Required()])
    apellidos = StringField("Apellidos:", validators=[Required()])
    genero = StringField("Genero:", validators=[Required()])
    fecha_nac = DateField("Fecha de Nacimiento", validators=[Required()])
    id_colonia = IntegerField("id_colonia", validators=[Required()])
    submit = SubmitField('Submit')

class TipoUrgenciaForm(Form):
    id_tipo_urgencia = IntegerField("id", validators=[Required()])
    urgencia = SelectField("Urgencia:", choices=[('EMBARAZO'),('ACCIDENTE'),('RESPIRATORIO'),('OTRO')], validators=[Required()])
    descripcion = StringField("Descripcion:", validators=[Required()])
    submit = SubmitField('Submit')

class MovimientoForm(Form):
    id_movimiento = IntegerField("id", validators=[Required()])
    id_paciente = IntegerField("id_paciente", validators=[Required()])
    id_usuario = IntegerField("id_usuario", validators=[Required()])
    id_hospital = IntegerField("id_hospital", validators=[Required()])
    id_ambulancia = IntegerField("id_ambulancia", validators=[Required()])
    id_tipo_urgencia = IntegerField("id_tipo_urgencia", validators=[Required()])
    fecha_inicio = DateTimeField('Fecha y Hora Inicial', validators=[Required()])
    fecha_final = DateTimeField('Fecha y Hora Final', validators=[Required()])
    presion_arterial = StringField('Presion Arterial', validators=[Required()])
    frec_cardiaca = StringField('Frecuencia Cardiaca', validators=[Required()])    
    frec_respiratoria = StringField('Frecuencia Respiratoria', validators=[Required()])
    temperatura = StringField('Temperatura', validators=[Required()])
    escala_glassglow = StringField('Escala Glassgow', validators=[Required()])
    gravedad = SelectField("Gravedad", choices=[('BAJA'),('MEDIA'),('ALTA'),('MUY ALTA')])
    submit = SubmitField('Submit')
    
class UsuarioForm(Form):
    id_usuario = IntegerField("id", validators=[Required()])
    id_tipo_usuario = SelectField("Tipo usuario:", choices=[('1'),('2'),('3'),('4')], validators=[Required()])
    nombre_usuario = StringField("Username:", validators=[Required()])
    password_hash = PasswordField("Password:", validators=[Required()])
    submit = SubmitField('Submit')
