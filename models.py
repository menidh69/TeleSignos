from app import db
from sqlalchemy.dialects.postgresql import JSON


class Municipio(db.Model):
    __tablename__ = 'municipios'

    id_municipio = db.Column(db.Integer, primary_key=True)
    nombre_municipio = db.Column(db.String(70))

    def __init__(self, nombre_municipio):
        self.nombre_municipio = nombre_municipio

    def __repr__(self):
        return '<id_municipio {}>'.format(self.id_municipio)

class Colonia(db.Model):
    __tablename__ = 'colonias'

    id_colonia = db.Column(db.Integer, primary_key=True)
    nombre_colonia = db.Column(db.String(70))
    id_municipio = db.Column(db.Integer)

    def __init__(self, nombre_colonia):
        self.nombre_colonia= nombre_colonia

    def __repr__(self):
        return '<id_colonia {}>'.format(self.id_colonia)

class Hospital(db.Model):
    __tablename__ = 'hospitales'

    id_hospital = db.Column(db.Integer, primary_key=True)
    id_municipio = db.Column(db.Integer)
    nombre_hospital = db.Column(db.String(70))
    direccion = db.Column(db.String(70))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(70))

    def __init__(self, nombre_hospital, direccion, telefono, email):
        self.nombre_hospital = nombre_hospital
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return '<id_hospital {}>'.format(self.id_hospital)

class Ambulancia(db.Model):
    __tablename__ = 'ambulancias'

    id_ambulancia = db.Column(db.Integer, primary_key=True)
    num_unidad = db.Column(db.String(10))
    id_servicio = db.Column(db.Integer)

    def __init__(self, num_unidad, id_servicio):
        self.num_unidad= num_unidad
        self.id_servicio = id_servicio

    def __repr__(self):
        return '<id_ambulancia {}>'.format(self.id_ambulancia)

class Servicio(db.Model):
    __tablename__ = 'servicios'

    id_servicio = db.Column(db.Integer, primary_key=True)
    servicio_nombre = db.Column(db.String(10))
    contacto = db.Column(db.String(70))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(70))

    def __init__(self, servicio_nombre, contacto, telefono, email):
        self.servicio_nombre = servicio_nombre
        self.contacto = contacto
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id_servicio)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(70))
    id_tipo_usuario = db.Column(db.Integer)
    

    def __init__(self, nombre_usuario, id_tipo_usuario):
        self.nombre_usuario = nombre_usuario
        self.id_tipo_usuario

    def __repr__(self):
        return '<id_usuario {}>'.format(self.id_usuario)
    
class Tipo_Usuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id_tipo_usuario = db.Column(db.Integer, primary_key=True)
    tipo_usuario = db.Column(db.String(70))
    registro = db.Column(db.Boolean)
    medico_reg = db.Column(db.Boolean)
    

    def __init__(self, tipo_usuario, registro, medico_reg):
        self.tipo_usuario = tipo_usuario
        self.registro = registro
        self.medico_reg = medico_reg

    def __repr__(self):
        return '<id_tipo_usuario {}>'.format(self.id_tipo_usuario)

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = db.Column(db.Integer, primary_key = True)
    servicio_medico = db.Column(db.String(70))
    nombre_paciente = db.Column(db.String(70))
    apellidos = db.Column(db.String(100))
    genero = db.Column(db.String(1))
    fecha_nac = db.Column(db.DateTime)
    id_colonia = db.Column(db.Integer)
  
    def __init__(self, servicio_medico, nombre_paciente, apellidos, genero, fecha_nac, id_colonia):
        self.servicio_medico = servicio_medico
        self.nombre_paciente = nombre_paciente
        self.apellidos = apellidos
        self.genero = genero
        self.fecha_nac = fecha_nac
        self.id_colonia = id_colonia

    def __repr__(self):
        return '<id_paciente {}>'.format(self.id_paciente)

class Movimientos(db.Model):
    __tablename__ = 'movimientos'

    id_movimiento = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    id_hospital = db.Column(db.Integer)
    id_ambulancia = db.Column(db.Integer)
    id_colonia = db.Column(db.Integer)
    id_urgencia = db.Column(db.Integer)
    fecha_inicio = db.Column(db.DateTime)
    fecha_final = db.Column(db.DateTime)
    presion_arterial = db.Column(db.String(10))
    frec_cardiaca = db.Column(db.String(10))
    frec_respiratoria = db.Column(db.String(10))
    temperatura = db.Column(db.String(2))
    escala_glassgow = db.Column(db.String(10))
    gravedad = db.Column(db.String(10))

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

    id_bitacora = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    id_movimiento = db.Column(db.Integer)
    tipo_movimiento = db.Column(db.Integer)

    def __init__(self, id_bitacora, fecha, id_movimiento, tipo_movimiento):
        self.fecha = fecha
        self.id_movimiento = id_movimiento
        self.tipo_movimiento = tipo_movimiento
    
    def __repr__(self):
        return '<id_bitacora {}>'.format(self.id_bitacora)

class Tipo_movimiento(db.Model):
    __tablename__='tipo_movimiento'

    id_tipo_movimiento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(70))

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
            return '<id_tipo_movimiento {}>'.format(self.id_tipo_movimiento)
