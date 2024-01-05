from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question


bp = Blueprint('question', __name__, url_prefix='/question') #여기서 main_views.py 매핑 구별

#render_template함수는 HTML파일을 렌더링하여 클라이언트에게 전송하는 역할
@bp.route('/list/')
def _list():
     #질문 목록 데이터/order_by는 결과를 정렬하는 함수
    #order_by(Question.create_date.desc())의 의미는 조회된 데이터를 작성일시 기준으로 역순으로 정렬하라는 의미.
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/',methods=('GET', 'POST'))
def create():
    form = QuestionForm() #인스턴스화
    #request.method는 create 함수로 요청된 전송 방식을 의미한다.
    #그리고 form.validate_on_submit 함수는 전송된 폼 데이터의 정합성을 점검한다.
    #DataRequired() 같은 점검 항목에 이상이 없는지 확인다.
    #질문 등록하기 누르면 get방식 요청이므로 질문 등록 화면을 보여주고
    #저장하기 버튼을 누르면 post방식 요청이므로 데이터베이스에 질문을 저장한다.
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form) 