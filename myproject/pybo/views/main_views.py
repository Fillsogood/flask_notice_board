from flask import Blueprint
#creat app 함수안에 매핑이 필요할 때마다 너무 길어져서 블루프린트로 체계적으로 관리
bp = Blueprint('main',__name__, url_prefix='/') #main은 bp의 별칭

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'