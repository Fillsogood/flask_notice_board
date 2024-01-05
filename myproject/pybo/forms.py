from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


#QuestionForm의 속성은 제목,내용이다. 글자수의 제한이 있는 제목의 경우StringField를 사용하고 
#제한 없는 내용은 TextAreaField를 사용한다.
#validators는 검증을 위해 사용되는 도구로 필수 항목인지를 체크하는 DataRequired 사용
# 그 외로 이메일인지를 체크하는Email,길이를 체크하는 Length등이 있다.
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

#답변 등록 폼
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

#회원가입 폼
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])