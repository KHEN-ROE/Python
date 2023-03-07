"""
#문자열에서 홀수 번째 문자 추출하기

string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)  # 출력값: "acegi"
"""

"""
#문자열 hello world에서 world 부분 문자열을 추출

string = "hello world"
substring = string[6:]
print(substring)  # "world"

#문자열 hello world에서 hlowrd 부분 문자열을 추출
string = "hello world"
substring = string[::2] #0 부터 두 칸 간격으로 잘라서 출력
print(substring)  # "hlowrd"

#문자열을 뒤집는 예제
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"

# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True

# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"

# 문자열 찾기 함수 예시
s = "hello, world!"

print(s.find("o"))  # 4
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2

# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "

#문자열 분리
string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

# 문자열 분리, 결합 함수 예시
s = "apple,banana,grape"

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"] #하나의 문자열을 분리

print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape" #하나의 문자열로 만듦

# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"
"""

"""
사용자가 입력한 문자열에 대해 다음 물음에 답하라
문자열의 문자수를 출력하라
문자열을 10번 반복한 문자열을 출력하라
문자열의 첫 번째 문자를 출력하라
문자열에서 처음 3문자를 출력하라
문자열에서 마지막 3문자를 출력하라
문자열의 문자를 거꾸로 출력하라
문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
문자를 모두 대문자로 변경하여 출력하라
문자를 모두 소문자로 변경하여 출력하라
문자열에서 'a'를 'e'로 대체하여 출력하라
"""
"""
str = input("문자열 입력")
print(len(str))
print(str*10)
print(str[0])
print(str[:3])
print(str[-3:])
print(str[::-1])
if len(str) >= 7:
    print(str[6])
else:
    print("문자 없음")
print(str[-1:1])
print(str.upper())
print(str.lower())
print(str.replace('a','e'))
"""

"""
문자 'a'가 들어가는 단어를 키보드에서 입력 받아
첫 번째 줄에는 'a'까지의 문자열을 출력하고
두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라. -- 다시 해볼것 
"""
"""
word = input("a가 들어가는 단어입력: ")

index_of_a = word.find('a')

if index_of_a == -1:
    print("a가 없음")
else:
    print(word[:index_of_a+1])
    print(word[index_of_a+1:])

#++ a가 여러개면??
print(word.replace('a','a\n'))
"""

"""
숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. --- 다시 해볼 것
str(12) -> '12'가 된다. 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다.
int('12') -> 12가 된다. 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라.
예를 들어 234 -> 2+3+4=9가 된다
[Hint]sum = 0
for s in '234':
    sum += int(s)
"""
"""
total_sum = 0  # 모든 숫자의 자리수 합을 누적할 변수 초기화

for num in range(1, 1001):  # 1부터 1000까지의 숫자에 대해서
    num_str = str(num)  # 숫자를 문자열로 변환
    digit_sum = 0  # 현재 숫자의 자리수 합을 저장할 변수 초기화
    
    for digit_char in num_str:  # 숫자의 각 자리수에 대해서
        digit_sum += int(digit_char)  # 자리수 합을 누적
        
    total_sum += digit_sum  # 현재 숫자의 자리수 합을 전체 합에 누적

print(total_sum)  # 전체 합 출력

#교수님 코드 -- ##13501 과 27004 둘 중 뭐가 답인가? 13501이 답
total = 0
for num in range(1, 1001):
    #각 자리수의 합을 구함
    digits_sum=0
    for digit in str(num):
        digits_sum += int(digit)
        #전체 합에 더함
        total += digits_sum
print(total)
"""

"""
#리스트 컴프리헨션(List Comprehension)
#파이썬에서 리스트를 간단하게 생성하는 방법 중 하나.

#1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
#반복문을 통해 나온 num이 if문을 만족할 때 맨 좌측의 num이 된다
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

#리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

#리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
fruit_lengths = [len(fruit) for fruit in words]
print(fruit_lengths)  # [5, 6, 6, 6]

#문자열 리스트에서 길이가 5 이상인 문자열만 대문자로 바꾸기
words = ["apple", "banana", "orange", "grape", "watermelon", "kiwi"]
result = [fruit.upper() for fruit in words if len(fruit) >= 5]
print(result)

#리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist] #중첩반복문. 맨 좌측의 변수에 집중하라
print(new_list)  # [1, 2, 3, 4, 5, 6]

#주어진 이차원 리스트에서 짝수만 리스트로 생성하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]

#리스트 슬라이싱
my_list = [1, 2, 3, 4, 5]
print(my_list[-3:])   # [3, 4, 5]
print(my_list[:-2])   # [1, 2, 3]

#리스트 합치기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
list3 = list1
print(list3) # 출력 결과: [1, 2, 3, 4, 5, 6]

#리스트 요소 수정, 추가, 제거하기
#인덱싱을 이용하여 요소 수정하기
my_list = [1, 2, 3, 4]
my_list[2] = 5
print(my_list) # 출력 결과: [1, 2, 5, 4]

#슬라이싱을 이용하여 요소 수정하기
my_list = [1, 2, 3, 4]
my_list[1:3] = [5, 6]
print(my_list) # 출력 결과: [1, 5, 6, 4]

#append() 메서드를 이용하여 요소 추가하기
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list) # 출력 결과: [1, 2, 3, 4, 5]

#insert() 메서드를 이용하여 요소 추가하기
my_list = [1, 2, 3, 4]
my_list.insert(2, 5)
print(my_list) # 출력 결과: [1, 2, 5, 3, 4]

#슬라이싱을 이용한 요소 제거
my_list = [1, 2, 3, 4, 5]
my_list[1:4] = []
print(my_list) # 출력 결과: [1, 5]

#del 키워드를 이용하여 요소 제거하기
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list) # 출력 결과: [1, 2, 4]

#remove() 메서드를 이용하여 요소 제거하기
my_list = [1, 2, 3, 4]
my_list.remove(3)
print(my_list) # 출력 결과: [1, 2, 4]

#pop() 메서드를 이용하여 요소 제거하기
my_list = [1, 2, 3, 4]
my_list.pop()
print(my_list) # 출력 결과: [1, 2, 3]

my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(2)
print(my_list) # 출력 결과: [1, 2, 4, 5]
print(removed_item) # 출력 결과: 3

#clear() 메서드를 이용한 요소 제거
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list) # 출력 결과: []

#sum 함수를 이용한 합 구하기
nums = [1, 2, 3, 4, 5]
total = sum(nums)
print(total)  # 15

#sorted 함수를 이용한 정렬하기
nums = [3, 5, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4, 5]

#reversed 함수를 이용한 역순 정렬하기
nums = [1, 2, 3, 4, 5]
reversed_nums = list(reversed(nums))
print(reversed_nums)  # [5, 4, 3, 2, 1]

#sort(): 리스트를 정렬합니다. 원본 리스트가 변경됩니다.
#sorted(): 리스트를 정렬합니다. 정렬된 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.
#sorted 는 내장함수. reverse 와 reversed 도 같은 맥락
#sort와 revere는 리스트의 함수. sorted와 reversed는 내장함수!

a = [3, 2, 1]
a.sort()
print(a)  # 출력: [1, 2, 3]

a = [3, 2, 1]
b = sorted(a)
print(a)  # 출력: [3, 2, 1]
print(b)  # 출력: [1, 2, 3]
"""

"""
a=[1,2,3]
b=reversed(a)
print(b) # 이터레이터라서 출력이 안 됨
c = list(b) # 따라서 list로 형변환 해준다 
print(c)
"""

#연습문제
"""
3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
insert()로 맨 앞에 새로운 친구 추가
insert()로 3번째 위치에 새로운 친구 추가
append()로 마지막에 친구 추가
"""
"""
name = ["홍길동", "김철수", "손흥민"]
name.insert(0, "호날두")
name.insert(2, "진양철")
name.append("차무식")
print(name)
"""

"""
리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
두 번째 요소를 17로 수정
리스트에 4, 5, 6을 추가
첫 번째 요소 제거
리스트를 요소 순서대로 배열하기
인덱스 3에 25넣기
"""
"""
lst = [1,2,3]
lst[1] = 17
lst2 = [4,5,6]
lst.extend(lst2)
lst3 = lst
del lst3[0]
lst3.sort()
lst3.insert(3,25)
print(lst3)
"""

"""
for 루프를 이용하여 다음과 같은 리스트를 생성하라.
0~49까지의 수로 구성되는 리스트
1~50까지 수의 제곱으로 구성되는 리스트
"""
"""
lst1 = [num for num in range(0, 51)]
print(lst1)

lst2 = [num*num for num in range(0, 51)]
print(lst2)
"""

"""
크기가 같은 두 개의 리스트 L, M을 생성하고
두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라.
예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성 -- 다시 할 것
"""
"""
l = [1,2,3]
m = [4,5,6]
result = []
for i in range(len(l)):
    result.append(l[i] + m[i])
print(result)
## 컴프리핸션 이용해서 풀면?
"""

"""
사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라.
예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.
"""
#혼자 해볼 것 hint : split, join
num_list=[]
num_list= input("숫자 입력")


"""
#튜플과 리스트 간 형변환 시 주의점
my_list = [1, 2, [3, 4]]
my_tuple = tuple(my_list)
print(my_tuple) # 출력 결과: (1, 2, [3, 4]) //내부에 있는 리스트는 값 변화가능!!

my_tuple[2][0] = 5
print(my_tuple) # 출력 결과: (1, 2, [5, 4])
"""

#튜플을 이용한 함수에서의 활용 예시
#튜플을 이용한 함수에서는 여러 값을 동시에 반환할 수 있으며,
#함수의 매개변수로서 튜플을 사용하여 함수에 여러 인수를 전달할 수 있습니다.
"""
def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide
result = calculate(10, 2)  #  결과: (12, 8, 20, 5.0)
print(result)
"""




