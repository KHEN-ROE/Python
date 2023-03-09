#함수
#연습문제
#1. 1~n까지의 합을 계산하는 함수

def sum(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    return sum
    
print(sum(10))

#반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성.
#이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라. --다시할 것

def cir_area(r):
    return 3.14*r**2
    

def cir_cirm(r):
    return 2*3.14*r

print(round(cir_area(3.5),1))
print(round(cir_cirm(3.5),1))

#den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성 --다시할 것
def den(n):
    cd=[]
    for i in range(1,n+1):
        if n%i==0:
            cd.append(i)
    return cd
print(den(12))

#함수 인자 전달 방식
# 인자의 순서와 조합 사용 예시
def print_numbers(a, b, *args, c=10, d=20):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
print_numbers(1, 2, 3, 4, 5, c=30, d=40)
# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5) args가 투플 형태로 출력된다

#지역변수 전역변수 
x = 2  # 전역 변수

def my_function():
    y = 2  # 지역 변수
    x = 1
    print('y:', y)
    print('x:', x)

my_function()
print('x:', x)


#지역변수와 전역번수 - global
x = 'global'

def my_function():
    global x #전역변수를 가져와서 쓴다.  #이걸 주석처리하면? 함수 내 지역변수만 사용 
    x = 'local'

my_function()
print(x)

##람다함수## - 가독성 높여줌 
# 기존 함수 정의 방법
def add(a, b):
    return a + b

# 람다 함수 정의 방법
lambda_add = lambda a, b: a + b

# 함수 호출
result1 = add(3, 4)             # 7
result2 = lambda_add(3, 4)      # 7

#함수의 인자로 전달된 예시, +반환값으로 사용할 수 도 있다.
students = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
]

# 점수(score)를 기준으로 학생 리스트 정렬
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
print(sorted_students)
# 출력 결과: [{'name': 'Bob', 'score': 90}, {'name': 'Alice', 'score': 80}, {'name': 'Charlie', 'score': 70}]

#내부함수
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func #함수를 리턴

result = outer_func(10)
print(result(20))  # 출력결과: 30 -- 다시 이해할 것

#내부 함수를 이용하여 간단한 계산기 함수를 구현한 예제
def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    return add, subtract, multiply, divide # 튜플(소괄호 생략)

add, subtract, multiply, divide = calculator() # 튜플을 언패킹 

print(add(10, 20))  # 출력결과: 30
print(subtract(10, 20))  # 출력결과: -10
print(multiply(10, 20))  # 출력결과: 200
print(divide(10, 20))  # 출력결과: 0.5

#코드의 재사용성을 높일 수 있다
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)  # 제곱 함수를 구현
cube = power(3)  # 세제곱 함수를 구현

print(square(3))  # 출력결과: 9
print(cube(3))  # 출력결과: 27

#함수 내 변수 참조 순서
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)
