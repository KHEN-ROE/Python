#그룹핑

#그룹핑 추출 예시
import re

phone_number = "02-1234-5678"
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)
print(result.group()) # 전체 출

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678

#그룹핑 치환 예시

import re
#날짜 표기법이 YYYY-MM-DD 형태로 되어 있을 때 이를 MM/DD/YYYY 형태로 바꾸고 싶다면
date = "2022-03-18"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2/\3/\1", date)

print(result)  # "03/18/2022"

#이름 순서 바꾸기
import re

# 이름 순서 바꾸기
string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)" #\s는 공백 의미
result = re.sub(pattern, r"\2 \1", string)
print(result)  # "Yuna Kim"



