from flask import Flask
app = Flask(__name__)
# 플라스크 애플리케이션을 생성하는 코드. name이라는 변수에 pybo.py 모듈이 담겨 실행
#name은 pybo라는 문자열이 담긴다. @app.route는 URL과 플라스크 코드를 매핑하는 데코레이터다
#즉 / URL이 요청이되면 플라스크는 hello_pybo함수를 실행 시킨다.
@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'