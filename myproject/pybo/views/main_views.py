from flask import Blueprint

bp = Blueprint('main',__name__, url_prefix='/') #main은 bp의 별칭

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'