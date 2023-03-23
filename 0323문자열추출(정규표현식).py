#문자열 추출 - 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하고 추출하는 과정
#findall 함수 예시
import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']