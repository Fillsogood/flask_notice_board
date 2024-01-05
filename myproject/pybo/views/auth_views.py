from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

#post방식에는 계정을 저장하고 Get방식에는 계정을 등록 화면을 출력한다.
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)#비밀번호는 폼으로 전달받은 값을 그대로 저장하지 않고enerate_password_hash함수로 암호화하여 저장
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

#POST방식에는 로그인을 수행하고, GET요청에는 로그인 화면을 보여준다.
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

#로그인 여부 확인
@bp.before_app_request #이 애너테이션이 적용된 함수는 라우팅 함수보다 항상 먼저 실행된다. 즉, 얖으로load_logged_in_user 함수는 모든 라우팅 함수보다 먼저 실행될 것이다.
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
    
#로그아웃 라우팅 함수
@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))