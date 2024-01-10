from flask import Flask
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# 플라스크 애플리케이션을 생성하는 코드. name이라는 변수에 pybo.py 모듈이 담겨 실행
#name은 pybo라는 문자열이 담긴다. @app.route는 URL과 플라스크 코드를 매핑하는 데코레이터다
#즉 / URL이 요청이되면 플라스크는 hello_pybo함수를 실행 시킨다.

def create_app(): #create app함수가 app 객체를 생성해 반환하도록 수정 이 함수가 애플리케이션 팩토리이다.
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views , question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    return app