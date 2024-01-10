from pybo import db

class Question(db.Model):#db.Model
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    #user_id속성은 User 모델을 Question 모델과 연결하기 위한 속성이고
    #user속성은 Question 모델에서 User 모델을 참조하기 위한 속성이다.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #question id 속성은 답변을 질문과 연결하기 위해 추가한 속성이다.
    #답변은 어떤 질문에 대한 답변이지 알아야 하므로 질문의 id 속성이 필요하다.
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #아이디가 자동으로 증가 하는 User모델의 기본키
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)#unique True로 설정하면 같은 값을 저장할 수 없게 만듬