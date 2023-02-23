# 변수 사용 예제
x = 10  # 변수 x에 정수 10을 저장
y = 20  # 변수 y에 정수 20을 저장
z = x + y  # 변수 z에 x와 y의 합을 저장
print(z)  # 변수 z의 값을 출력

import keyword

print("keyword : ",keyword.kwlist)

# 10진수
x = 42
print(x)    # 출력: 42

# 2진수
y = 0b101010
print(y)    # 출력: 42

# 8진수
z = 0o52
print(z)    # 출력: 42

# 16진수
w = 0x2a
print(w)    # 출력: 42

#일반적인 소수점 표기법: 3.14, -2.5, 100.0
#지수 표기법: 3e8 (3 x 10의 8제곱), 1.23e-4 (0.000123)
#float() 함수를 사용하여 실수로 변환: float(10), float("3.14") " " 안의 값은 문자임. 이걸 실수로 저장하겠다는 뜻
#다른 연산의 결과로 생성: 7 / 2 (결과는 3.5)

# 복소수 생성
z1 = 2 + 3j
z2 = complex(4, -2)

# 복소수 연산
z3 = z1 + z2
z4 = z1 * z2
z5 = z1 / z2
z6 = z1 ** 2

# 결과 출력
print(z3)   # (6+1j)
print(z4)   # (14+8j)
print(z5)   # (-0.4+0.7j)
print(z6)   # (-5+12j)

string = "Hello, World!"
position = string.find("World")
print(position) # 7 출력


'''
num = 10
text = "apple"
print(num + text)
'''

num = 10
text = "apple"
print(str(num) + text)

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)

fruits = {"apple": 3, "banana": 2, "cherry": 5}
print(fruits)
print(fruits["banana"])
fruits["orange"] = 4
print(fruits)

result = 2 + 3 * 4 - 6 / 2 ** 2
print(result)  

# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력
print("k" not in b)  # True 출력

# 산술식 및 비교식 응용 예제
x = 10
y = 5
a = x + y
b = x - y
c = x * y
d = x / y

if a > c and b < d:  # a가 c보다 크고, b가 d보다 작은 경우
    print("a > c and b < d")  # 출력 안 됨
elif a < c or b > d:  # a가 c보다 작거나, b가 d보다 큰 경우
    print("a < c or b > d")  # "a < c or b > d" 출력
else:
    print("neither")  # 출력 안 됨

# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30

# 딕셔너리 출력 예제
person = {"name": "John", "age": 25, "city": "New York"}
print(person)  # {'name': 'John', 'age': 25, 'city': 'New York'} 출력

# 딕셔너리 값 출력 예제
print(person["name"])  # 'John' 출력
print(person["age"])  # 25 출력
print(person["city"])  # 'New York' 출력

# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

msg = "My name is %s, I'm %d years old, and my height is %.1f." % (name, age, height)
print(msg)
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 출력 형식 지정 예제
num = 10
pi = 3.14159265

print("num = %d" % num)  # 출력 결과: "num = 10"
print("pi = %f" % pi)  # 출력 결과: "pi = 3.141593"
print("pi = %.2f" % pi)  # 출력 결과: "pi = 3.14"
print("pi = %10.2f" % pi)  # 출력 결과: "pi =       3.14"

# format() 메소드를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is {2}, I'm {0} years old, and my height is {2:.1f}.".format(name, age, height)) #{:.f} 실수에 대하여 :이하의 옵션으로 출력하겠다. format 함수 이용하면 인덱스 이용하여 다르게 출력가
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

#예제
name = "Tom"
age = 27
print("My name is %s and I am %d years old." %(name,age))

a=3
b=2
c=1
print("I have {2} apples, {0} oranges, {1} bananas.".format(a,b,c))

r = 1.23
print(f"The result is {r:.2f}")

s=90
print(f"your score is {s}%")

a1=10
a2=20
a3=a1+a2
print(f"{a1}+{a2}={a3}")

'''
# input() 함수를 이용하여 사용자로부터 입력받아 계산하기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division:.2f}")

# input(), 포매팅, 산술식을 이용하여 계산하기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

#하나의 문자열로 만들기
result = f""" 
입력한 숫자:
첫 번째 숫자: {num1}
두 번째 숫자: {num2}

산술 연산 결과:
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} * {num2} = {num1 * num2}
{num1} / {num2} = {num1 / num2:.2f}
"""
print(result)
'''

#예제1 : 구매할 사과의 총가격 구하기
anum = int(input("구매할 사과의 개수를 입력하세요: "))
aprice = int(input("구매할 사과의 가격 : "))
atax = float(input("부가세율 : "))
atax1 = atax/100

totalprice = (anum*aprice) + (anum*aprice)*atax1 
print(f"vat가 포함된 사과의 최종가격은 {int(totalprice)} 원 입니다")

#예제2) 초를 입력하면 분과 초로 표시하는 프로그램. ex)200초 : 3분 20초
second = int(input("초를 입력하세요 : "))
result = second/60
charge = second%60

print(f"입력하신 {second}초 는 {int(result)}분 {charge}초 입니다.")

#예제3) 분(min)을 입력하면 일, 시간, 분으로 출력하는 프로그램 ex)1550분은 1일 1시간 50분
min = int(input("input minute"))
hour = min/60
day = hour/24
hour1 = hour%24
min1 = min%60

print(f"{min}분은 {int(day)}일 {int(hour1)}시간 {min1}분 입니다.")

#예제4) 500만원을 연이율 5% 복리로 저금했을 때 5년 후 원리금의 합계 출력
money = int(input("금액을 입력하세요"))
rate = float(input("이율을 입력하세요"))
rate1 = rate/100
year = int(input("저축하실 기간을 입력하세요"))
money1 = money * ((1+rate1)**year)

print(f"{year}년 후 원리금의 합계는 {int(money1)}원 입니다")

#예제5) 1부터 n까지의 합은 n(n+1)/2로 주어진다. 1부터 100까지의 합을 구하여 출력
num = int(input("input number"))
sum = num*(num+1) /2

print(f"1부터 {num}까지의 합은 {int(sum)}입니다")

#예제6) 판매자가 딸기와 포도를 판매중이다. 포도한 알의 무게는 75g, 딸기 한 알의 무게는 113.5g.
        #포도 알의 개수와 딸기의 개수 입력받아 총 무게 계산
wG = 75
wS = 113.5
numG = int(input("포도 알의 개수 입력"))
numS = int(input("딸기 알의 개수 입력"))
wSum = numG*wG + numS*wS
print(f"포도 알 {numG}개와 딸기 알 {numS}개를 합한 총 중량은 {int(wSum)}g 입니다")
