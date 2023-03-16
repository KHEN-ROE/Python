"""
#내장 함수
a=bin(12)   #'0b1100'
print(a)

int('123') #123
int('1010', 2) #10

#enumerate
color = ['red','black','blue']
print(color)
for index, color in enumerate(color):
    print(index,color)
    
#eval
result=eval('2+3 *4')
print(result)

#filter - 시퀀스의 각 요소에 대해 함수를 적용하여 결과가 True인 것만 모아서 리스트로 반환
numbers = [1,2,3,4,5,6,7]

result = list(filter(lambda x: x%2==0, numbers))
print(result)
"""

#map - 시퀀스의 각 원소에 대해 지정된 함수를 적용하여, 새로운 리스트를 반환
numbers = [1,2,3,4,5]
result = list(map(lambda x:x**2, numbers))
print(result)

#ord - ch에 대한 ASCII 코드 반환
a = ord('A')
print(a)

#repr - obj를 문자열로 변환
b = repr(b'0011')
print(b)
my_list = [1,2,3]
list_str = repr(my_list)
print(list_str)

#round - 실수 x를 소수점 아래 n자리로 반올림하여 반환
num1 = 3.141592653589793238
num2 = 2.71828182845904523536

result=round(num1)
result1=round(num2,3)
print(result)
print(result1)

#zip - seq 요소와 *seqs 요소의 튜플 쌍으로 이루어진 리스트 iterable 반환
names = ['Alice', 'KEN', 'ROE']
ages = [24,25,66]

for name, age in zip(names, ages):
    print(name,age)
