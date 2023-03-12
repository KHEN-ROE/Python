"""
다음 딕셔너리에 대해 물음에 답하라. days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
"""

"""
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
month = input("input month")
print(days[month])
"""

"""
#알파벳 순서로 모든 월을 출력하라
n = sorted(days)
print(n)
"""
"""
n = sorted(days.keys())
print(n)
"""
"""
#일수가 31인 월을 모두 출력하라
for i in days:
    if days[i]==31: # 키에 해당하는 value가 31 이면 해당 키 프린트 
        print(i)
"""

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
"""
키와 값 교환
일수를 기준으로 정렬
다시 이름이 앞으로 오게 바꿈
"""
"""
days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
days_item = days.items()
days_item = [ (day, month) for (month, day) in days_item] #위치 바꿈
days_item.sort() # 정렬하고
days_item = [ (month, day) for (day, month) in days_item] #다시 위치 바꿈
print(days_item)
"""

"""
#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month = input("월의 3자리만 입력")
for x in days:
    if x[0:3] == month.title(): # title 함수 - 첫글자 대문자, 나머지 소문자 변환 
        print(days[x])
"""
"""
days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
month = input("3자리 입력")
for x in days: # 그냥 days 하면 키값을 순회한다는 뜻 
    if x[0:3] == month.title():
        print(days[x]) #딕셔너리에서 해당하는 인덱스의 value 리턴 
"""


"""
다음 딕셔너리에 대해 물음에 답하라.
1 전화번호가 8로 끝나는 사용자 이름을 출력하라
2 이메일이 없는 사용자 이름을 출력하라
3 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
"""
"""
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for x in d:
    if x['phone'][7] == '8': # 키가 phone인 값의 7번째 인덱스 값이 8이면 
        print(x['name'])

for x in d:
    if x['email'] == '':
        print(x['name'])
        
        
name = input("input name")
flag =1;
for x in d:
    if x['name']==name.title():
        print(x['phone'], x['email'])
        flag=0;
if flag==1:
    print("없는 사람입니다")
# 딕셔너리 다시 공부할 것. 딕셔너리 - 키와 값으로 구성 
"""
"""
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for x in d:
    if x['phone'][7] == '8':
        print(x['name'])

for x in d:
    if x['email'] == '':
        print(x['name'])

name = input("input name")
for x in d:
    if x['name'] == name:
        print(x['phone'], x['email'])
    elif x['name'] != name:
        print("일치하는 정보 없음")
        break
"""

"""
#set 예제
#1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램 -- 다시 해볼 것

import random
pick = set()# 이게 뭘 의미? pick이라는 빈 set 생성 

while len(pick)<6:
    pick.add(random.randint(1,45))

print(sorted(pick))# sort() 함수 안되는 이유? sort는 리스트 정렬하는 함수임 
"""

#연습문제
#학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
"""
grade = {"Alice": [85, 90, 95],"Bob": [75, 80, 85],"Charlie": [95, 95, 95]}


for name, grade_list in grade.items():
    print(name, sum(grade_list)/len(grade_list))
"""

"""
grade = {"Alice": [85, 90, 95],"Bob": [75, 80, 85],"Charlie": [95, 95, 95]}

for name, grade in grade.items():
    print(name, sum(grade) / len(grade))
"""    

"""    
#숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
num = [1, 2, 2, 3, 3, 3, 4, 4, 5]
num = set(num)
num = sum(num)
print(num)
"""

"""
#주어진 문자열에서 각 알파벳의 빈도 수를 구하는 프로그램을 작성하시오. -- 다시할 것


chfr = {}

for c in text:
    if c.isalpha(): #이렇게 하면 공백 컴마 느낌표 출력안됨
        if c in chfr:
            chfr[c] += 1
        else:
            chfr[c] = 1

for c, count in chfr.items():
    print(c, count)
"""

"""
#교수님 코드
freq_dict = {} # 빈 set 생성 

for char in text: # text 순회
    if char not in freq_dict:  # text에서 가져온 값이 빈 set에 없으면 
        freq_dict[char] = 1 # text를 순회한 x 값과 1을 둘 다 저장
    else:
        freq_dict[char] += 1 # 키와 값 모두 저장

for c, count in freq_dict.items():
    print(c, count)
"""
"""
text = "Hello, world!"

arr = {}

for x in text:
    if x not in arr:
        arr[x] = 1
    else:
        arr[x] += 1
for c, count in arr.items():
    print(c, count)
"""


"""
두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.

리스트A: 임의의 길이와 요소를 가진 리스트
리스트B: 임의의 길이와 요소를 가진 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10] -- 다시 할 것
# 공통된 요소인 2와 4를 모두 포함한 리스트를 반환한다.
# 결과값
# [2, 4]
"""
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
list3=[]

for x in list1:
    if x in list2:
        list3.insert(0, x)
print(sorted(list3))
