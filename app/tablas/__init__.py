from flask import Blueprint

tablas = Blueprint('tablas', __name__) 

from . import views, errors