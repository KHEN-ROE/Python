#정규표현식
# match 함수 예시
import re

# 문자열의 시작부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")


# search 함수 예시
import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
pattern = r"[pP]ython"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")
    

    

