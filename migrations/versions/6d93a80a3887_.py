"""empty message

Revision ID: 6d93a80a3887
Revises: 554bc67e7ec5
Create Date: 2020-08-03 14:43:17.602249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d93a80a3887'
down_revision = '554bc67e7ec5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_urgencia',
    sa.Column('id_tipo_urgencia', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id_tipo_urgencia'),
    schema='public'
    )
    op.drop_table('urgencia')
    op.drop_constraint('ambulancias_id_servicio_fkey', 'ambulancias', type_='foreignkey')
    op.create_foreign_key(None, 'ambulancias', 'servicios', ['id_servicio'], ['id_servicio'], source_schema='public', referent_schema='public')
    op.drop_constraint('bitacora_id_movimiento_fkey', 'bitacora', type_='foreignkey')
    op.create_foreign_key(None, 'bitacora', 'movimientos', ['id_movimiento'], ['id_movimiento'], source_schema='public', referent_schema='public')
    op.drop_constraint('colonias_id_municipio_fkey', 'colonias', type_='foreignkey')
    op.create_foreign_key(None, 'colonias', 'municipios', ['id_municipio'], ['id_municipio'], source_schema='public', referent_schema='public')
    op.drop_constraint('hospitales_id_municipio_fkey', 'hospitales', type_='foreignkey')
    op.create_foreign_key(None, 'hospitales', 'municipios', ['id_municipio'], ['id_municipio'], source_schema='public', referent_schema='public')
    op.add_column('movimientos', sa.Column('id_tipo_urgencia', sa.Integer(), nullable=False))
    op.drop_constraint('movimientos_id_paciente_fkey', 'movimientos', type_='foreignkey')
    op.drop_constraint('movimientos_id_usuario_fkey', 'movimientos', type_='foreignkey')
    op.drop_constraint('movimientos_id_ambulancia_fkey', 'movimientos', type_='foreignkey')
    op.drop_constraint('movimientos_id_hospital_fkey', 'movimientos', type_='foreignkey')
    op.create_foreign_key(None, 'movimientos', 'tipo_urgencia', ['id_tipo_urgencia'], ['id_tipo_urgencia'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'movimientos', 'ambulancias', ['id_ambulancia'], ['id_ambulancia'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'movimientos', 'pacientes', ['id_paciente'], ['id_paciente'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'movimientos', 'hospitales', ['id_hospital'], ['id_hospital'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'movimientos', 'usuarios', ['id_usuario'], ['id_usuario'], source_schema='public', referent_schema='public')
    op.drop_column('movimientos', 'id_colonia')
    op.drop_constraint('pacientes_id_colonia_fkey', 'pacientes', type_='foreignkey')
    op.create_foreign_key(None, 'pacientes', 'colonias', ['id_colonia'], ['id_colonia'], source_schema='public', referent_schema='public')
    op.drop_constraint('usuarios_id_tipo_usuario_fkey', 'usuarios', type_='foreignkey')
    op.create_foreign_key(None, 'usuarios', 'tipo_usuario', ['id_tipo_usuario'], ['id_tipo_usuario'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'usuarios', schema='public', type_='foreignkey')
    op.create_foreign_key('usuarios_id_tipo_usuario_fkey', 'usuarios', 'tipo_usuario', ['id_tipo_usuario'], ['id_tipo_usuario'])
    op.drop_constraint(None, 'pacientes', schema='public', type_='foreignkey')
    op.create_foreign_key('pacientes_id_colonia_fkey', 'pacientes', 'colonias', ['id_colonia'], ['id_colonia'])
    op.add_column('movimientos', sa.Column('id_colonia', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'movimientos', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'movimientos', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'movimientos', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'movimientos', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'movimientos', schema='public', type_='foreignkey')
    op.create_foreign_key('movimientos_id_hospital_fkey', 'movimientos', 'hospitales', ['id_hospital'], ['id_hospital'])
    op.create_foreign_key('movimientos_id_ambulancia_fkey', 'movimientos', 'ambulancias', ['id_ambulancia'], ['id_ambulancia'])
    op.create_foreign_key('movimientos_id_usuario_fkey', 'movimientos', 'usuarios', ['id_usuario'], ['id_usuario'])
    op.create_foreign_key('movimientos_id_paciente_fkey', 'movimientos', 'pacientes', ['id_paciente'], ['id_paciente'])
    op.drop_column('movimientos', 'id_tipo_urgencia')
    op.drop_constraint(None, 'hospitales', schema='public', type_='foreignkey')
    op.create_foreign_key('hospitales_id_municipio_fkey', 'hospitales', 'municipios', ['id_municipio'], ['id_municipio'])
    op.drop_constraint(None, 'colonias', schema='public', type_='foreignkey')
    op.create_foreign_key('colonias_id_municipio_fkey', 'colonias', 'municipios', ['id_municipio'], ['id_municipio'])
    op.drop_constraint(None, 'bitacora', schema='public', type_='foreignkey')
    op.create_foreign_key('bitacora_id_movimiento_fkey', 'bitacora', 'movimientos', ['id_movimiento'], ['id_movimiento'])
    op.drop_constraint(None, 'ambulancias', schema='public', type_='foreignkey')
    op.create_foreign_key('ambulancias_id_servicio_fkey', 'ambulancias', 'servicios', ['id_servicio'], ['id_servicio'])
    op.create_table('urgencia',
    sa.Column('id_urgencia', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=70), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_urgencia', name='urgencia_pkey')
    )
    op.drop_table('tipo_urgencia', schema='public')
    # ### end Alembic commands ###
