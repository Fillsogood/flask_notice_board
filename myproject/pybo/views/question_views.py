from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question') #여기서 main_views.py 매핑 구별


@bp.route('/list/')
def _list():
     #질문 목록 데이터/order_by는 결과를 정렬하는 함수
    #order_by(Question.create_date.desc())의 의미는 조회된 데이터를 작성일시 기준으로 역순으로 정렬하라는 의미.
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question) 