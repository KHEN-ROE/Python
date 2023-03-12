#함수 연습문제
#1. 두 개의 매개변수 n, m을 전달받아 m x n개의 '*' 를 출력하는 함수를 작성하라
#예: 2, 4 -> ****
#			 ****
def box(n, m):
    for i in range(n): #n이 행의 개수
        print("*" * m) #m은 열의 개수. 줄 바꿈은 자동으로 되네 ? 
box(2,4)


#2 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성예: 123 -> 1+2+3 = 6
"""
def sum(n):
    sum = 0;
    a = int(n/100)
    a1 = int(n%100)
    b = int(a1/10)
    b1 = int(a1%10)
    
    if a1 == 0:
        sum = a
    elif a1 != 0:
        sum = a
        sum += b
        if b1 != 0:
            sum += b1
            
    return sum
print(round(sum(541)))
"""

#3 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
"""
def loc(s1, s2):
    for i in range(len(s1)): # range로 설정하니까 s1[i] 즉 인덱스 이용할 수 있네?. 그냥 in s1 하니까 사용 안되고.(이건 리스트가 아니라 그런듯) 
        if s1[i] != s2[i]:
            return i
            
s1 = "abcdefg"
s2 = "abcdeff"

print(loc(s1,s2))
"""
#gpt 코드
"""
def find_first_difference(str1, str2):
    
    #Finds the first position where two strings differ. Returns -1 if the two strings are equal.
    
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
    if len(str1) != len(str2):
        return min(len(str1), len(str2))
    return -1
"""
            

#4문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def location(str, c):
    list1=[]
    for i in range(len(str)):
        if str[i] == c:
            list1.insert(0, i)
    return sorted(list1)
str = "hello"
c = 'l'
print(location(str, c))

#5재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
sum=0
def reculsum(n):
    if n==1:
        return 1
    else:
        return n + reculsum(n-1)
print(reculsum(100))
            
    
    

