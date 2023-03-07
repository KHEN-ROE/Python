"""
#3/2 조건문
# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")
"""
"""
# 사용자로부터 성적을 입력받아, 학점 부여하기
score = int(input("성적을 입력하세요: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")
"""

"""
#한 문장의 if-else문
num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)

score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)
"""

"""
score = int(input("성적입력"))
if score>=90:
    grade = 'a'
elif score >=80:
    grade = 'b'
print(grade)
"""

"""
#세 개의 수 중 가장 작은 수를 출력하는 프로그램
a = 10
b = 20
c = 5
min_value = a
if a < b and a < c
else (b if b < c else c)
print("가장 작은 수는", min_value, "입니다.")
"""

""" 세 개의 수 비교 내가 만든 코드"""
"""
a=10
b=20
c=5
min=100
if a<min:
    min=a
if a<b:
    min=a
elif a>b:
    min=b
if a<c:
    min=a
elif a>c:
    min=c
print("min",min)
"""


"""
#사용자로부터 입력받은 수가 양수인 경우에만 제곱근을 구하고, 그 외에는 "잘못된 입력입니다."라는 메시지를 출력하는 프로그램
import math

num = float(input("양수를 입력하세요: "))

result = math.sqrt(num) if num > 0 else "잘못된 입력입니다."

print("결과: ", result)
"""

"""
#성적 계산기 작성 프로그램 - 직접 해본 코드 
num1 = float(input("국어 성적 입력"))
num2 = float(input("영어 성적 입력"))
num3 = float(input("수학 성적 입력"))
avg1 = num1/1
avg2 = num2/1
avg3 = num3/1

totalAvg = (num1*0.4)+(num2*0.4)+(num3*0.2)

if totalAvg >=90:
    grade='a'
elif totalAvg >=80:
    grade='b'
elif totalAvg >=70:
    grade='c'
elif totalAvg >=60:
    grade='d'
else:
    grade='f'

print(f"국어 : {num1:.0f}점 영어 : {num2:.0f}점 수학 : {num3:.0f}점")
print(f"각 과목의 평균점수 : {avg1:.2f}점, {avg2:.2f}점, {avg3:.2f}점")
print(f"총 평균점수 : {totalAvg:.2f}")
print(f"학점 : {grade}")
"""



"""
#연습문제
#사용자로부터 cm 단위의 길이를 입력 받는다. 입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고 양수이면 길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 1인치 = 2.54cm
num = int(input("길이를 입력하세요(cm)"))

if num <= 0 :
    print("잘못된 입력")
else:
    num1 = num * 2.54
    print(f"{num1}인치")
"""

"""
#사용자로부터 이수한 학점을 입력 받는다. 학점이 40학점 미만이면 "1학년입니다"를 출력하고, 40이상 80미만이면 "2학년입니다"를 출력한다. 학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.
score = int(input("학점 입력"))

if score < 40:
    print("1학년")
elif score >=40 and score < 80:
    print("2학년")
else:
    print("졸업반")
"""


#사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다. 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다. 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
"""
hour = int(input("현재 시간 입력(1~12)"))
while True:
    apm = int(input("am(1) or pm(2)"))
    if apm ==1 or apm==2:
        break
    else:
        print("wrong input, please input 1 or 2")
        continue

overtime = int(input("경과 시간"))

newhour = hour + (overtime%24)

if apm == 1:
    if newhour <= 12:
        print("최종시각", newhour,"am")
    else:
        if newhour-12 ==12:
            print("최종시각", newhour-12,"am")
        else:
            print("최종시각", newhour-12,"pm")
        

else:
    if newhour <= 12:
        print("최종시각", newhour,"pm")
    else:
        print("최종시각", newhour-24,"am")


# -- 혼자 다시 해볼 것. %, am pm 조건 이용하여
"""

"""
#반복문 while
#1에서부터 100까지의 짝수를 출력하는 예제
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
"""

"""
#사용자로부터 값을 입력 받아, 입력한 값이 0이 아닌 동안 입력한 값들의 합을 출력하는 예제
sum = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    sum += num
print("입력한 값들의 합: ", sum)
"""

"""
#10진수를 입력 받아 2진수로 변환하여 출력하는 프로그램
num = int(input("10진수를 입력하세요: "))
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2 #//는 몫
print("입력한 수의 2진수 표현: ", binary) #print(f"") 안써도 ',' 써서 구분하여 출력 가능
"""

"""
#for문
#리스트에 저장된 모든 수의 합을 구하는 코드
numbers = [1, 2, 3, 4, 5] #리스트는 []
sum = 0
for num in numbers:
    sum += num
print(sum)
"""

"""
#튜플의 원소를 순차적으로 출력하는 예제
colors = ("red", "green", "blue") # 튜플은 ()

for color in colors:
    print(color)
"""

"""
#문자열의 각 문자를 순차적으로 출력하는 예제
text = "Python"

for char in text:
    print(char)

# range 함수 이용하여 1부터 10까지의 숫자 출력하기
for i in range(1, 11):
    print(i)

#1부터 10까지의 숫자 중 짝수만 출력하기
for i in range(2, 11, 2):
    print(i)

#10부터 1까지 거꾸로 출력하기
for i in range(10, 0, -1):
    print(i)

# 0에서 4까지의 정수 시퀀스 생성
for i in range(5):
    print(i)

# 2에서 8까지 2씩 증가하는 정수 시퀀스 생성
for i in range(2, 9, 2):
    print(i)

# 10에서 1까지 1씩 감소하는 정수 시퀀스 생성
for i in range(10, 0, -1):
    print(i)

#구구단을 출력하는 예시
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
        
#별문자로 모양 그리기
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="") # print("*", end="\n")이게 숨겨진 기본옵션인데 그걸 바꿔줌
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
"""

"""
#연습문제
#3의 배수와 5의 배수의 합 구하기 -- 접근은 비슷하게 했는데 num%3 하고 있었음... 그리고 or가 아니라 and를 써서 틀림
num = int(input("양의 정수 입력"))
sum = 0
for i in range(1, num+1):
    if i % 3 ==0 or i % 5 ==0:
        sum += i
    
"""
"""
num = int(input("양의 정수 입력"))
sum = 0
for i in range(1, num+1):
    if i % 3 ==0 or i % 5 ==0:
        sum += i
print(sum)
"""


"""
print(f"1부터 10까지 수 중 3,5배수의 합은 {sum}")
    
#최댓값과 최솟값 찾기
#리스트 쓰지 말고 숫자 들어올 때마다 최댓값 최솟값 판별
max=0;
min=100;
for i in range(5):
    num = int(input(f"[최댓값 최솟값 찾기]\n\n{i+1}번째 숫자 입력: "))
    
    if num>max:
        max=num
        
    if num<min:
        min=num
        
print(f"최댓값은 {max} 최솟값은 {min}")

#숫자의 합이 100보다 작을 때까지 입력받기
sum=0;
while True:
    num = int(input("숫자를 입력하세요: "))
    sum += num
    if sum > 100:
        break
print(sum)
"""


#피보나치 수열의 n번째 항을 출력하는 프로그램 -- 다시 해볼 것
"""
n = int(input("몇 번째 항 출력?"))
if n==1 or n==2:
    result =1
else:
    a,b=1,1
    i=3
    while i <= n:
        result = a+b
        a=b
        b=result
        i+=1
            
print(f"피보나치 수열의 {n}번째 항은 {result}입니다")
"""

"""
#피보나치 gpt 코드
# First two terms of the sequence
n = int(input("Enter the number of terms: "))

a=1
b=1

# Loop to generate the sequence
for i in range(n-2):
    c = a + b
    a=b
    b=c
# Output the nth term of the sequence
print("The {}th term of the Fibonacci sequence is: {}".format(n, c))
"""


"""
#pass
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
"""

"""
#입력한 문자열에서 모음(a, e, i, o, u)을 제거하는 프로그램 pass 사용 예제
vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")

output_str = ""
for char in input_str:
    if char in vowels:
        pass
    else:
        output_str += char

print("Modified string:", output_str)
"""
"""
#숫자 맞추기 게임 
import random

secret_number = random.randint(1, 100) # 1부터 100 사이의 임의의 수를 선택합니다

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로 반복문을 종료합니다
"""

"""
#주사위 게임
#두 주사위를 던졌을 때, 합이 7이 되면 이김, 그렇지 않으면 지는 주사위 게임. randint() 함수 사용
#반복문 사용해서 이길 때까지 주사위 굴리기
import random
while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    print(f"주사위1 : {dice1} 주사위2: {dice2} 합 : {dice_sum}")
    if dice_sum ==7:
        print("you win")
        break
    else :
        print("throw again")
"""

"""
#게임 프로그램
#플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다.
#맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
#동전을 던져서 나오는 수는 다음 문장을 이용하라.
#from random import randint
#coin = randint(1,2) --- 1 또는 2를 임의로 발생
import random
money = 50
while True:
    coin = random.randint(1,2)
    guess = int(input("select 1 or 2 : " ))
    if guess == coin:
        money = money +9
        print(f"이겼습니다. 잔액은 {money}입니다")
        if money > 100:
            break
    else:
        money = money -10
        print(f"졌습니다. 잔액은 {money}입니다")
        if money < 0:
            break
"""

"""
두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
예를 들어 (16, 24)의 최대 공약수는 8이다.
두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을 작성하라.
큰 수를 작은 수로 나눈 나머지를 구하라
큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
작은 수가 0이 될 때까지 이 과정을 반목하라. 마지막 큰 수가 최대 공약수이다.
"""

"""
num1 = int(input("input num1 : "))
num2 = int(input("input num2 : "))
grd=0;
while True:
    remainder = num2%num1
    num2 = num1
    num1 = remainder
    if num1 ==0 :
        break
grd = num2
print(f"최대공약수는 {grd}")
"""




