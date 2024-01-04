from flask import Blueprint, url_for
from werkzeug.utils import redirect
#creat app 함수안에 매핑이 필요할 때마다 너무 길어져서 블루프린트로 체계적으로 관리
bp = Blueprint('main',__name__, url_prefix='/') #main은 bp의 별칭

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    #redirect함수는 입력받은 URL로 리다이렉트하고, url_for함수는 라우팅 함수명으로 URL알 역으로 찾는 함수이다.
    #redirect(URL) - URL로 페이지를 이동
    #url_for(라우팅 함수명) - 라우팅 함수에 매핑되어 있는 URL을 리턴
    return redirect(url_for('question._list')) # 즉 여기서 /question/list/  URL를 반환한다.