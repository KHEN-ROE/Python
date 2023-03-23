#모드에 따른 파일 열기
# 읽기 모드로 파일을 엽니다.
file = open("example.txt", "r")
content = file.read()
print("읽기 모드 예시:")
print(content)
file.close()

# 쓰기 모드로 파일을 엽니다.
file = open("example.txt", "w")
file.write("This is an example.\n")
file.write("We are writing to a file.\n")
print("쓰기 모드 예시:")
print("파일이 생성되었습니다.")
file.close()

# 추가 모드로 파일을 엽니다.
file = open("example.txt", "a")
file.write("We are appending to a file.\n")
print("추가 모드 예시:")
print("파일이 열렸고 내용이 추가되었습니다.")
file.close()


# 배타적 생성 모드로 파일을 엽니다.
file = open("example2.txt", "x")
file.write("This is a new file.\n")
print("배타적 생성 모드 예시:")
print("새로운 파일이 생성되었습니다.")
file.close()

# 이진 모드로 파일을 엽니다.
file = open("example.bin", "wb")
file.write(b"This is binary data.")
print("이진 모드 예시:")
print("바이너리 파일이 생성되었습니다.")
file.close()

# 읽기와 쓰기를 지원하는 모드로 파일을 엽니다.
file = open("example.txt", "r+")
content = file.read()
print("읽기와 쓰기를 지원하는 모드 예시:")
print("파일 내용:")
print(content)
file.write("\nWe are writing to the file again.")
file.close()



