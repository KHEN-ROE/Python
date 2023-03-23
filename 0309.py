"""
다음 딕셔너리에 대해 물음에 답하라.days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
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
#일수가 31인 월을 모두 출력하라
for i in days:
    if days[i]==31:
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

#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month = input("월의 3자리만 입력")
for x in days:
    if x[0:3] == month.title():
        print(days[x])
"""

"""
다음 딕셔너리에 대해 물음에 답하라.
전화번호가 8로 끝나는 사용자 이름을 출력하라
이메일이 없는 사용자 이름을 출력하라
사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
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
flag =1;
for x in d:
    if x['name']==name.title():
        print(x['phone'], x['email'])
        flag=0;
if flag==1:
    print("없는 사람입니다")
# 딕셔너리 다시 공부할 것
"""
"""
#set 예제
#1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램 -- 다시 해볼 것

import random
pick = set()

while len(pick)<6:
    pick.add(random.randint(1,45))

print(sorted(pick))
"""

#연습문제
#학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
grade = {"Alice": [85, 90, 95],"Bob": [75, 80, 85],"Charlie": [95, 95, 95]}


for name, grade_list in grade.items():
    print(name, sum(grade_list)/len(grade_list))
    
#숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
num = [1, 2, 2, 3, 3, 3, 4, 4, 5]
num1 = set(num)
sum1 = sum(num1)
print(sum1)

#주어진 문자열에서 각 알파벳의 빈도 수를 구하는 프로그램을 작성하시오. -- 다시할 것
text = "Hello, world!"

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
#교수님 코드
freq_dict = {}

for char in text:
    if char not in freq_dict:
        freq_dict[char] = 1
    else:
        freq_dict[char] += 1

for c, count in freq_dict.items():
    print(c, count)
"""
    
"""
두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.

리스트A: 임의의 길이와 요소를 가진 리스트
리스트B: 임의의 길이와 요소를 가진 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10] -- 다시 할 것
"""
