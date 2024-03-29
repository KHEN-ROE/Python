#예외처리 연습문제
"""
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6} 이 주어질 때
try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.

사용자로부터 문자열을 입력 받는다
문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다
문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.

"""
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
while True:
    try:
        str = input("input day")
        value = data[str]
        print(value)
    except KeyError:
        print("해당하는 요일 없음")
        break

#나의 코드
try:
    str1 = input("input day")
    for x in data:
        if str1 == x:
            print(data[str1])
except KeyError:
    print("해당하는 요일 없음")


#try-except 안쓰고 만들기    
user_input = input("input day")
value = data.get(user_input, None)
if value is not None:
    print(value)
else:
    print("항목없음")