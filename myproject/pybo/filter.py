# 필터에 사용한 날짜 포맷 코드
# %Y년,%m월,%d일,%p AM/PM(오전,오후 구분),%I시간(0~12시로 표현),%M분 
#format_datetime함수는 전달받은 datetime 객체(value)를 날짜포맷형식(fmt)
#에 맞게 변환하여 리턴하는 함수이다.
def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)