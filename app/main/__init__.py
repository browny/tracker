from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/parser')

from . import views
