from app import db
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
import enum

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class UrgenciaEnum(enum.Enum):
    EMBARAZO='embarazo'
    ACCIDENTE='accidente'
    RESPIRATORIO='respiratorio'
    OTRO='otro'

class Gravedad(enum.Enum):
    BAJA='baja'
    MEDIA='media'
    ALTA='alta'
    MUY_ALTA='muy alta'

class tipoUsuario(enum.Enum):
    PARAMEDICO='paramédico'
    MEDICO_REG='medico regulador'
    REGISTRANTE='registrante'
    ADMIN='admin'

class Municipio(db.Model):
    __tablename__ = 'municipios'
    __table_args__ = {"schema": "public"}

    id_municipio = db.Column(db.Integer, primary_key=True)
    nombre_municipio = db.Column(db.String(70))
    colonias = db.relationship('Colonia', backref='municipio', lazy=True)
    hospitales = db.relationship('Hospital', backref='municipio', lazy=True)


    def __init__(self, nombre_municipio):
        self.nombre_municipio = nombre_municipio

    def __repr__(self):
        return '<id_municipio {}>'.format(self.id_municipio)

class Colonia(db.Model):
    __tablename__ = 'colonias'
    __table_args__ = {"schema": "public"}

    id_colonia = db.Column(db.Integer, primary_key=True)
    nombre_colonia = db.Column(db.String(70))
    id_municipio = db.Column(db.Integer, db.ForeignKey('public.municipios.id_municipio'), nullable=False)
    pacientes = db.relationship('Paciente', backref='colonia', lazy=True)


    def __init__(self, nombre_colonia):
        self.nombre_colonia= nombre_colonia

    def __repr__(self):
        return '<id_colonia {}>'.format(self.id_colonia)

class Hospital(db.Model):
    __tablename__ = 'hospitales'
    __table_args__ = {"schema": "public"}

    id_hospital = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_municipio = db.Column(db.Integer, db.ForeignKey('public.municipios.id_municipio'), nullable=False)
    nombre_hospital = db.Column(db.String(70))
    direccion = db.Column(db.String(70))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(70))
    movimientos = db.relationship('Movimiento', backref='hospital', lazy=True)

    def __init__(self, nombre_hospital, direccion, telefono, email):
        self.nombre_hospital = nombre_hospital
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return '<id_hospital {}>'.format(self.id_hospital)

class Servicio(db.Model):
    __tablename__ = 'servicios'
    __table_args__ = {"schema": "public"}

    id_servicio = db.Column(db.Integer, primary_key=True)
    servicio_nombre = db.Column(db.String(10))
    contacto = db.Column(db.String(70))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(70))
    ambulancias = db.relationship('Ambulancia', backref='servicio', lazy=True)

    def __init__(self, servicio_nombre, contacto, telefono, email):
        self.servicio_nombre = servicio_nombre
        self.contacto = contacto
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id_servicio)

class Ambulancia(db.Model):
    __tablename__ = 'ambulancias'
    __table_args__ = {"schema": "public"}

    id_ambulancia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_unidad = db.Column(db.String(10))
    id_servicio = db.Column(db.Integer, db.ForeignKey('public.servicios.id_servicio'), nullable=False)
    movimientos = db.relationship('Movimiento', backref='ambulancia', lazy=True)


    def __init__(self, num_unidad):
        self.num_unidad= num_unidad
        

    def __repr__(self):
        return '<id_ambulancia {}>'.format(self.id_ambulancia)

class Tipo_Usuario(db.Model):
    __tablename__ = 'tipo_usuario'
    __table_args__ = {"schema": "public"}

    id_tipo_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_usuario = db.Column(db.Enum(tipoUsuario))
    registro = db.Column(db.Boolean)
    medico_reg = db.Column(db.Boolean)
    usuarios = db.relationship('Usuario', backref='tipo_usuario', lazy=True)

    def __init__(self, tipo_usuario, registro, medico_reg):
        self.tipo_usuario = tipo_usuario
        self.registro = registro
        self.medico_reg = medico_reg

    def __repr__(self):
        return '<id_tipo_usuario {}>'.format(self.id_tipo_usuario)

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {"schema": "public"}

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_usuario = db.Column(db.String(70), unique=True, index=True)
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('public.tipo_usuario.id_tipo_usuario'), nullable=False)
    movimientos = db.relationship('Movimiento', backref='usuario', lazy=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.id_usuario)

    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def __repr__(self):
        return '<id_usuario {}>'.format(self.id_usuario)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    __table_args__ = {"schema": "public"}

    id_paciente = db.Column(db.Integer, primary_key = True, autoincrement=True)
    servicio_medico = db.Column(db.String(70))
    nombre_paciente = db.Column(db.String(70))
    apellidos = db.Column(db.String(100))
    genero = db.Column(db.String(1))
    fecha_nac = db.Column(db.DateTime)
    id_colonia = db.Column(db.Integer, db.ForeignKey('public.colonias.id_colonia'), nullable=False)
    movimientos = db.relationship('Movimiento', backref='paciente', lazy=True)
  
    def __init__(self, servicio_medico, nombre_paciente, apellidos, genero, fecha_nac, id_colonia):
        self.servicio_medico = servicio_medico
        self.nombre_paciente = nombre_paciente
        self.apellidos = apellidos
        self.genero = genero
        self.fecha_nac = fecha_nac
        self.id_colonia = id_colonia

    def __repr__(self):
        return '<id_paciente {}>'.format(self.id_paciente)

class Tipo_Urgencia(db.Model):
    __tablename__= 'tipo_urgencia'
    __table_args__ = {'schema': 'public'}

    id_tipo_urgencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    urgencia = db.Enum(UrgenciaEnum)
    descripcion = db.Column(db.String(70))
    movimientos = db.relationship('Movimiento', backref='tipo_urgencia', lazy=True)

    def __init__(self, urgencia, descripcion):
        self.urgencia = urgencia
        self.descripcion = descripcion

    def __repr__(self):
        return '<id_tipo_urgencia {}>'.format(self.id_tipo_urgencia)


class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    __table_args__ = {"schema": "public"}

    id_movimiento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('public.pacientes.id_paciente'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('public.usuarios.id_usuario'), nullable=False)
    id_hospital = db.Column(db.Integer, db.ForeignKey('public.hospitales.id_hospital'), nullable=False)
    id_ambulancia = db.Column(db.Integer, db.ForeignKey('public.ambulancias.id_ambulancia'), nullable=False)
    id_tipo_urgencia = db.Column(db.Integer, db.ForeignKey('public.tipo_urgencia.id_tipo_urgencia'), nullable=False)
    fecha_inicio = db.Column(db.DateTime)
    fecha_final = db.Column(db.DateTime)
    presion_arterial = db.Column(db.String(10))
    frec_cardiaca = db.Column(db.String(10))
    frec_respiratoria = db.Column(db.String(10))
    temperatura = db.Column(db.String(2))
    escala_glassgow = db.Column(db.String(10))
    gravedad = db.Column(db.Enum(Gravedad))
    registros = db.relationship('Bitacora', backref='movimientos', lazy=True)
    

    def __init__(self, id_movimiento, id_paciente, id_usuario, id_hospital, 
    id_ambulancia, id_colonia, id_urgencia, fecha_inicio, fecha_final, presion_arterial, frec_cardiaca, frec_respiratoria,
    temperatura, escala_glassgow, gravedad):
        self.id_movimiento = id_movimiento
        self.id_paciente = id_paciente
        self.id_usuario = id_usuario
        self.id_hospital = id_hospital
        self.id_ambulancia = id_ambulancia
        self.id_colonia = id_colonia
        self.id_urgencia = id_urgencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.presion_arterial = presion_arterial
        self.frec_cardiaca = frec_cardiaca
        self.frec_respiratoria = frec_respiratoria
        self.temperatura = temperatura
        self.escala_glassgow = escala_glassgow
        self.gravedad = gravedad

    def __repr__(self):
        return '<id_movimiento {}>'.format(self.id_movimiento)

class Bitacora(db.Model):
    __tablename__ = 'bitacora'
    __table_args__ = {"schema": "public"}

    id_bitacora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime)
    id_movimiento = db.Column(db.Integer, db.ForeignKey('public.movimientos.id_movimiento'))
    tipo_movimiento = db.Column(db.Integer)


    def __init__(self, id_bitacora, fecha, id_movimiento, tipo_movimiento):
        self.fecha = fecha
        self.id_movimiento = id_movimiento
        self.tipo_movimiento = tipo_movimiento
    
    def __repr__(self):
        return '<id_bitacora {}>'.format(self.id_bitacora)



# class Tipo_movimiento(db.Model):
#     __tablename__='tipo_movimiento'

#     id_tipo_movimiento = db.Column(db.Integer, primary_key=True)
#     descripcion = db.Column(db.String(70))

#     def __init__(self, descripcion):
#         self.descripcion = descripcion

#     def __repr__(self):
#             return '<id_tipo_movimiento {}>'.format(self.id_tipo_movimiento)
