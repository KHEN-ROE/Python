"""
#파일 읽기
file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)

file.seek(0)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print(line)

file.seek(0)

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
lines = file.readlines()
print(lines)

file.seek(0)

file.close()  # 파일을 닫습니다.


#파일쓰기
file = open("example2.txt", "w") # "a" 하면 뒤에다가 내용 추가함

# 파일에 문자열을 씁니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")

# 파일에 문자열의 리스트를 씁니다.
lines = ["We will use it to demonstrate file writing in Python.\n",
         "We can write multiple lines at once.\n"]
file.writelines(lines)

file.close()  # 파일을 닫습니다.
"""

#파일 닫기
#with 문은 파일을 열고 작업을 마치면 파일을 자동으로 닫아줍니다.
with open("example.txt", "r") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print(content)

