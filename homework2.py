"""
1. Analyze a Sentence
문장 입력받아서 부호 지우고 처음과 끝 단어만 출력
"""

"""
import string
text = input("input text")
text2 = text.translate(str.maketrans('','',string.punctuation))

text3 = text2.split()
print("First word : " + text3[0])
print("Last word : " + text3[len(text3)-1])
"""

#2. 3-part 이름 입력 받아서 미들네임만 출력
"""
import string
name = input("input name")

name1 = name.split()
print(name1[1])
"""

#3. 중앙값 출력
"""
import statistics as st

numbers = int(input("How many numbers do you want to enter?"))

numList = []

for i in range(numbers):
    numList.append(float(input("Enter a number")))

print("median : ", st.median(numList))
"""

#4. puzzle
"""
Starting_word = 'NAISNIENLGELTETWEORRSD'
word1=""
word2=""

for i in range(len(Starting_word)):
    if i % 2 == 0:
        word1 += Starting_word[i] + " "
    else:
        word2 += Starting_word[i] + " "
print(word1)
print(word2)
"""

#5. Special Number
"""
init = 1000
while True:
    init = init + 1
    reverseNum = int(str(init)[::-1]) #[::-1] 은 시퀀스 뒤집는 슬라이싱. start:stop:step. 앞에 두개 생략하고 끝에서 부터 시작한다는 의미
    if init * 4 == reverseNum:
        print(init)

    if init >= 10000:
        break
"""

#6. 중복되지 않는 문자열의 개수

#7. pay raise

def salary(fName, lName, cSalary):
    newSalary = 0
    if cSalary < 40000:
        newSalary = cSalary * 1.05
    elif cSalary >= 40000:
        newSalary = (cSalary + 2000) + cSalary * 0.02
    return print(f"new salary for {fName} {lName} : {newSalary}")

fName = input("first name")
lName = input("last name")
cSalary = int(input("current salary"))

salary(fName, lName, cSalary)
