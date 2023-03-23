#정규표현식을 활용한 실제 예제
#이메일 주소 추출
import re

def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #\.은 .을 찾겠다는 의미, [A-Z|a-z]는 대문자 혹은 소문자, {2,}는 2개 이상
                # \b는 단어의 경게를 나타내는 메타문자 
    emails = re.findall(pattern, string)
    return emails


string = "Ken's email is shdnrnjs@gmail.com. another email is doxx707@nate.com"

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']

#메일 주소의 유효성을 검증하는 예제
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False

#전화번호 유효성 검증하는 예제
import re

def is_valid_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3,4}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_number1 = '010-1234-5678'
phone_number2 = '02-123-4567'
phone_number3 = '123-4567'

print(is_valid_phone_number(phone_number1))  # True
print(is_valid_phone_number(phone_number2))  # True
print(is_valid_phone_number(phone_number3))  # False

#로그 데이터에서 IP 주소를 추출하는 예시
import re

log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)
