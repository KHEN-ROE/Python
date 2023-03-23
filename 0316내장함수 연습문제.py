#내장함수 연습문제
"""
enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서
'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라.
'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.
"""

"""
str = input("문자열 입력")
for index, str in enumerate(str):
    if str=='a':
        print(index)
"""

"""
두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고,
'2'를 입력하면 sub(), '3'을 입력하면 mul(),
'4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.
!!! 참고로 딕셔너리는 인덱싱 불가!!!
"""
"""
def sum(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def mul(a,b):
    result = a*b
    return result

def div(a,b):
    result = a/b
    return result
num = int(input("input num"))
dict = {1:sum(10,20), 2:sub(10,20), 3:mul(10,20), 4:div(10,20)}
if num == 1:
    print(dict[1])
elif num == 2 :
    print(dict[2])
elif num== 3:
    print(dict[3])
elif num==4:
    print(dict[4])
"""
    
"""
다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수 작성
예: 문자열 'led=on&motor=off&switch=off'이고
구분 문자가 '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환
Hint: dict([['a','b'], ['c', 'd']])  {'a': 'b', 'c': 'd'}
"""
"""
str = 'led=on&motor=off&switch=off'
myDict={}
def mkdict(str):
    str1 = str.split('&') # &기준으로 잘라서 리스트로 반환
    for x in str1:
        key, value = x.split('=') # 리스트를 = 기준으로 잘라서 키,값으로 반환
        myDict[key] = value # 딕셔너리 키에 값 저장 
    return myDict # 딕셔너리 반환 

print(mkdict(str))
"""

"""
str1 = str.split('&')
print(str1)
for x in str1:
    key, value = x.split('=')
    print(key)
    print(value)
    myDict[key]=value
    print(myDict)
"""

#안보고 다시
myDict = {} # 빈 딕셔너리 생성
str = 'led=on&motor=off&switch=off'

def mkdict(str):
    str1 = str.split("&") # &기준으로 잘라서 리스트로 변환
    #그러면 리스트를 순회하면서 = 기준으로 자르고, 딕셔너리에 저장해야지
    for x in str1:
        key, value = x.split('=') # 키와 값에 저장
        myDict[key] = value # 딕셔너리의 키에 값 저장
    return myDict # 딕셔너리 반환

#함수 호출
print(mkdict(str))
    
