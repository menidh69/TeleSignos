from flask import request
from flask_restful import Resource
from .. models import Movimiento, Paciente, Municipio, Colonia, Hospital, Ambulancia, Tipo_Urgencia, Servicio
from .. import api
from app import ma


#----------SCHEMA------------------------

class MunicipioSchema(ma.Schema):
    class Meta:
        fields = ("id_municipio","nombre_municipio")
    

class ColoniaSchema(ma.Schema):
    class Meta:
        fields = ("id_colonia","nombre_colonia", "id_municipio")
    
class HospitalSchema(ma.Schema):
    class Meta:
        fields = ("id_hospital", "id_municipio", "nombre_hospital", 
    "direccion", "telefono", "email")

class ServicioSchema(ma.Schema):
    class Meta:
        fields = ("id_servicio,", "servicio_nombre", "contacto", "telefono", "email")

class AmbulanciaSchema(ma.Schema):
    class Meta:
        fields = ("id_ambulancia", "num_unidad", "id_servicio")

class PacienteSchema(ma.Schema):
    class Meta:
        fields = ("id_paciente", "servicio_medico", "nombre_paciente", "apellidos", "genero", "fecha_nac", "id_colonia")

class Tipo_UrgenciaSchema(ma.Schema):
    class Meta:
        fields = ("id_tipo_urgencia," "urgencia", "descripcion")

class MovimientoSchema(ma.Schema):
    class Meta:
        fields = ("id_movimiento", "id_paciente", "id_usuario", "id_hospital", "id_ambulancia", "id_tipo_urgencia"
    "fecha_inicio", "fecha_final", "presion_arterial", "frec_cardiaca", "frec_respiratoria", "temperatura", "escala_glassgow"
    "gravedad")


municipio_schema = MunicipioSchema()
municipios_schema = MunicipioSchema(many=True)
colonia_schema = ColoniaSchema()
colonias_schema = ColoniaSchema(many=True)
hospital_schema = HospitalSchema()
hospitales_schema = HospitalSchema(many=True)
paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)
servicio_schema = ServicioSchema()
servicios_schema = ServicioSchema(many=True)
ambulancia_schema = AmbulanciaSchema()
ambulancias_schema = AmbulanciaSchema(many=True)
tipo_urgencia_schema = Tipo_UrgenciaSchema()
tipos_urgencia_schema = Tipo_UrgenciaSchema(many=True)
movimiento_schema = MovimientoSchema()
movimientos_schema = MovimientoSchema(many=True)

#------------RESOURCES----------------

#----------municipio---------------
class MunicipiosResource(Resource):
    def get(self):
        if request.args:
            args = request.args
            if 'nombre' in args:
                nombre = args['nombre']
                search = "%{}%".format(nombre)
                municipios = Municipio.query.filter(Municipio.nombre_municipio.like(search)).all()
                return municipios_schema.dump(municipios)
        else:
            municipios = Municipio.query.all()
            return municipios_schema.dump(municipios)
    
    #new
    def post(self):
        new_municipio = Municipio(
            id_municipio=request.json['id_municipio'],
            nombre_municipio=request.json['nombre_municipio']
        )
        db.session.add(new_municipio)
        db.session.commit()
        return municipio_schema.dump(new_municipio)

class MunicipioResource(Resource):
    def get(self, id_municipio):
        municipio = Municipio.query.get_or_404(id_municipio)
        return municipio_schema.dump(municipio)

    def patch(self, id_municipio):
        municipio = Municipio.query.get_or_404(id_municipio)

        if 'id_municipio' in request.json:
            municipio.id_municipio = request.json['id_municipio']
        if 'nombre_municipio' in request.json:
            municipio.nombre_municipio = request.json['nombre_municipio']

        db.session.commit()
        return municipio_schema.dump(municipio)
    
    def delete(self, id_municipio):
        municipio = Municipio.query.get_or_404(id_municipio)
        db.session.delete(municipio)
        db.session.commit()
        return '', 204


#-----------colonias--------------
class ColoniasResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            colonias = Colonia.query.filter_by(**args).all()
            return colonias_schema.dump(colonias)
        else:
            colonias = Colonia.query.all()
            return colonias_schema.dump(colonias)
    
    def post(self):
        new_colonia = Colonia(
            id_colonia=request.json['id_colonia'],
            nombre_colonia=request.json['nombre_colonia'],
            id_municipio=request.json['id_municipio']
        )
        db.session.add(new_colonia)
        db.session.commit()
        return colonia_schema.dump(new_colonia)

class ColoniaResource(Resource):
    def get(self, id):
        colonia = Colonia.query.get_or_404(id)
        return colonia_schema.dump(colonia)
    
    def patch(self, id):
        colonia = Colonia.query.get_or_404(id)

        if 'id_colonia' in request.json:
            colonia.id_colonia = request.json['id_colonia']
        if 'nombre_colonia' in request.json:
            colonia.nombre_colonia = request.json['nombre_colonia']
        if 'id_municipio' in request.json:
            colonia.id_municipio = request.json['id_municipio']
        
        db.session.commit()
        return colonia_schema.dump(colonia)
    
    def delete(self, id):
        colonia = Colonia.query.get_or_404(id)
        db.session.delete(colonia)
        db.session.commit()
        return '', 204

#-----------hospitales-----------------
class HospitalesResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            hospitales = Hospital.query.filter_by(**args).all()
            return hospitales_schema.dump(hospitales)       
        else:
            hospitales = Hospital.query.all()
            return hospitales_schema.dump(hospitales)
    
    def post(self):
        new_hospital = Hospital(
            id_municipio=request.json['id_municipio'],
            nombre_hospital=request.json['nombre_hospital'],
            direccion=request.json['direccion'],
            telefono=request.json['telefono'],
            email=request.json['email']
        )
        db.session.add(new_hospital)
        db.session.commit()
        return colonia_schema.dump(new_hospital)

class HospitalResource(Resource):
    def get(self, id):
        hospital = Hospital.query.get_or_404(id)
        return hospital_schema.dump(hospital)

    def patch(self, id):
        hospital = Hospital.query.get_or_404(id)
        if 'id_hospital' in request.json:
            hospital.id_hospital = request.json['id_hospital']
        if 'id_municipio' in request.json:
            hospital.id_municipio = request.json['id_municipio']
        if 'nombre_hospital' in request.json:
            hospital.nombre_hospital = request.json['nombre_hospital']
        if 'direccion' in request.json:
            hospital.direccion = request.json['direccion']
        if 'telefono' in request.json:
            hospital.telefono = request.json['telefono']
        if 'email' in request.json:
            hospital.email = request.json['email']
        db.session.commit()
        return hospital_schema.dump(hospital)

    def delete(self, id):
        hospital = Hospital.query.get_or_404(id)
        db.session.delete(hospital)
        db.session.commit()
        return '', 204

#------------ambulancias-----------------
class AmbulanciasResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            ambulancias = Ambulancia.query.filter_by(**args).all()
            return ambulancias_schema.dump(ambulancias)
        else:
            ambulancias = Ambulancia.query.all()
            return ambulancias_schema.dump(ambulancias)
    
    def post(self):
        new_ambulancia = Ambulancia(
            num_unidad=request.json['num_unidad'],
            id_servicio=request.json['num_unidad']
        )
        db.session.add(new_ambulancia)
        db.session.commit()
        return ambulancia_schema.dump(new_ambulancia)

class AmbulanciaResource(Resource):
    def get(self, id):
        ambulancia = Ambulancia.query.get_or_404(id)
        return amulancia_schema.dump(ambulancia)

    def patch(self, id):
        ambulancia = Ambulancia.query.get_or_404(id)
        if 'num_unidad' in request.json:
            ambulancia.num_unidad = request.json['num_unidad']
        if 'id_servicio' in request.json:
            ambulancia.id_servicio = request.json['id_servicio']
        db.session.commit()
        return ambulancia.schema.dump(ambulancia)

    def delete(self, id):
        ambulancia = Ambulancia.query.get_or_404(id)
        db.session.delete(ambulancia)
        db.session.commit()
        return '', 204

#------------servicios--------------------
class ServiciosResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            servicios = Servicio.query.filter_by(**args).all()
            return servicios_schema.dump(servicios)
        else:
            servicios = Servicio.query.all()
            return servicios_schema.dump(servicios)
    
    def post(self):
        new_servicio = Servicio(
            servicio_nombre=request.json['servicio_nombre'],
            contacto = request.json['contacto'],
            telefono = request.json['telefono'],
            email = request.json['email']
        )
        db.session.add(new_servicio)
        db.session.commit()
        return servicio_schema.dump(new_servicio)

class ServicioResource(Resource):
    def get(self, id):
        servicio = Servicio.query.get_or_404(id)
        return servicio_schema.dump(servicio)
    
    def patch(self, id):
        servicio = Servicio.query.get_or_404(id)
        if 'servicio_nombre' in request.json:
            servicio.servicio_nombre = request.json['servicio_nombre']
        if 'contacto' in request.json:
            servicio.contacto = request.json['contacto']
        if 'telefono' in request.json:
            servicio.telefono = request.json['telefono']
        if 'email' in request.json:
            servicio.email = request.json['email']
        db.session.commit()
        return servicio_schema.dump(servicio)
    
    def delete(self, id):
        servicio = Servicio.query.get_or_404(id)
        db.session.delete(servicio)
        db.session.commit()
        return '', 204
       
#------------pacientes--------------------
class PacientesResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            pacientes = Paciente.query.filter_by(**args).all()
            return pacientes_schema.dump(pacientes)
        else:
            pacientes = Paciente.query.all()
            return pacientes_schema.dump(pacientes)
    
    def post(self):
        paciente = Paciente(
            servicio_medico = request.json['servicio_medico'],
            nombre_paciente = request.json['nombre_paciente'],
            apellidos = request.json['apellidos'],
            genero = request.json['genero'],
            fecha_nac = request.json['fecha_nac'],
            id_colonia = request.json['id_colonia']
        )
        db.session.add(paciente)
        db.session.commit()
        return paciente_schema.dump(paciente)
    
class PacienteResource(Resource):
    def get(self, id):
        paciente = Paciente.query.get_or_404(id)
        return paciente_schema.dump(paciente)

    def patch(self, id):
        paciente = Paciente.query.get_or_404(id)
        if 'servicio_medico' in request.json:
            paciente.servicio_medico = request.json['servicio_medico']
        if 'nombre_paciente' in request.json:
            paciente.nombre_paciente = request.json['nombre_paciente']
        if 'apellidos' in request.json:
            paciente.apellidos = request.json['apellidos']
        if 'genero' in request.json:
            paciente.genero = request.json['genero']
        if 'fecha_nac' in request.json:
            paciente.fecha_nac = request.json['fecha_nac']
        if 'id_colonia' in request.json:
            paciente.fecha_nac = request.json['id_colonia']
        db.session.commit()
        return paciente_schema.dump(paciente)
    
    def delete(self, id):
        paciente = Paciente.query.get_or_404(id)
        db.session.delete(paciente)
        db.session.commit()
        return '', 204

#-----------movimientos--------------------

class MovimientosResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            movimientos = Movimiento.query.filter_by(**args).all()
            return movimientos_schema.dump(movimientos)
        else:
            movimientos = Movimiento.query.all()
            return movimientos_schema.dump(movimientos)
    
    def post(self):
        movimiento = Movimiento(
            id_ambulancia=request.json['id_ambulancia'],
            id_colonia=request.json['id_colonia'],
            id_urgencia=request.json['id_urgencia']
        )
        db.session.add(movimiento)
        db.session.commit()
        return movimiento_schema.dump(movimiento)

class MovimientoResource(Resource):
    def get(self, id):
        movimiento = Movimiento.query.get_or_404(id)
        return movimiento_schema.dump(movimiento)
    
    def patch(self, id):
        movimiento = Movimiento.query.get_or_404(id)
        if 'id_paciente' in request.json:
            movimiento.id_paciente = request.json['id_paciente']
        if 'id_usuario' in request.json:
            movimiento.id_usuario = request.json['id_usuario']
        if 'id_hospital' in request.json:
            movimiento.id_hospital = request.json['id_hospital']
        if 'id_ambulancia' in request.json:
            movimiento.id_ambulancia = request.json['id_ambulancia']
        if 'id_tipo_urgencia' in request.json:
            movimiento.id_tipo_urgencia = request.json['id_tipo_urgencia']
        if 'fecha_inicio' in request.json:
            movimiento.fecha_inicio = request.json['fecha_inicio']
        if 'fecha_final' in request.json:
            movimiento.fecha_final = request.json['fecha_final']
        if 'presion_arterial' in request.json:
            movimiento.presion_arterial = request.json['presion_arterial']
        if 'frec_cardiaca' in request.json:
            movimiento.frec_cardiaca = request.json['frec_cardiaca']
        if 'frec_respiratoria' in request.json:
            movimiento.frec_respiratoria = request.json['frec_respiratoria']
        if 'temperatura' in request.json:
            movimiento.temperatura = request.json['temperatura']
        if 'escala_glassgow' in request.json:
            movimiento.escala_glassgow = request.json['escala_glassgow']
        if 'gravedad' in request.json:
            movimiento.gravedad = request.json['gravedad']
        db.session.commit()
        return movimiento_schema.dump(movimiento)

    def delete(self, id):
        movimiento = Movimiento.query.get_or_404(id)
        db.session.delete(movimiento)
        db.session.commit()
        return '', 204

#-----------tipo_urgencia-------------------

class Tipos_UrgenciaResource(Resource):
    def get(self):
        if request.args:
            args = request.args.to_dict()
            tipos = Tipo_Urgencia.query.filter_by(**args).all()
            return tipos_urgencia_schema.dump(tipos)
        else:
            tipos_urgencia = Tipo_Urgencia.query.all()
            return tipos_urgencia_schema.dump(tipos_urgencia)
    
    def post(self):
        tipo_urgencia = Tipo_Urgencia(
            urgencia = request.json['tipo_urgencia'],
            descripcion = request.json['urgencia']
        )
        db.session.add(tipo_urgencia)
        db.session.commit()
        return tipo_urgencia_schema.dump(tipo_urgencia)

class Tipo_UrgenciaResource(Resource):
    def get(self, id):
        tipo_urgencia = Tipo_Urgencia.query.get_or_404(id)
        return tipo_urgencia_schema.dump(tipo_urgencia)
    
    def patch(self,id):
        tipo_urgencia = Tipo_Urgencia.query.get_or_404(id)
        if 'urgencia' in request.json:
            tipo_urgencia.urgencia = request.json['urgencia']
        if 'descripcion' in request.json:
            tipo_urgencia.descripcion = request.json['descripcion']
        db.session.commit()
        return tipo_urgencia_schema.dump(tipo_urgencia)
    
    def delete(self, id):
        tipo_urgencia = Tipo_Urgencia.query.get_or_404(id)
        db.session.delete(tipo_urgencia)
        db.session.commit()
        return '', 204

api.add_resource(Tipos_UrgenciaResource, '/api/tipos_urgencia')
api.add_resource(Tipo_UrgenciaResource, '/api/tipo_urgencia/<int:id>')
api.add_resource(MovimientoResource, '/api/movimiento/<int:id>')
api.add_resource(MovimientosResource, '/api/movimientos')
api.add_resource(PacientesResource, '/api/pacientes')
api.add_resource(PacienteResource, '/api/paciente/<int:id>')
api.add_resource(ServicioResource, '/api/servicio/<int:id>')
api.add_resource(ServiciosResource, '/api/servicios')
api.add_resource(AmbulanciasResource, '/api/ambulancias')
api.add_resource(AmbulanciaResource, '/api/ambulancia/<int:id>')
api.add_resource(HospitalesResource, '/api/hospitales')
api.add_resource(HospitalResource, '/api/hospital/<int:id>')
api.add_resource(ColoniasResource, '/api/colonias')
api.add_resource(ColoniaResource, '/api/colonia/<int:id>')
api.add_resource(MunicipiosResource, '/api/municipios')
api.add_resource(MunicipioResource, '/api/municipio/<int:id_municipio>')


if __name__ == '__main__':
    app.run(debug=True)