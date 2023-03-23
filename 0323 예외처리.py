#예외처리

#ValueError 처리 예시
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")

#FileNotFoundError 처리 예시
try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist. Please check the file path.")

#한 개의 except 블록으로 여러 예외 처리: 
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

#각각의 예외를 별도의 except 블록으로 처리:
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#as 키워드를 사용하여 에러 메시지 표시
try:
    result = 5 / 0
except ZeroDivisionError as error:
    print(f"An error occurred: {error}")

#모든 예외 처리 예시
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")

#try-except-else 문의 구조:
"""
try:
    # 예외가 발생할 수 있는 코드
except [예외 타입]:
    # 예외가 발생했을 때 실행할 코드
else:
    # 예외가 발생하지 않았을 때 실행할 코드
"""
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"You entered the number {number}.")

#파일 읽기 예시
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
    file.close()

#try-except-finally 문의 구조:
"""
try:
    # 예외가 발생할 수 있는 코드
except ExceptionType1:
    # 예외 타입 1이 발생한 경우 실행할 코드
except ExceptionType2:
    # 예외 타입 2가 발생한 경우 실행할 코드
# ... 필요한 만큼의 except 블록을 추가
finally:
    # 예외 발생 여부와 상관없이 항상 실행할 코드
"""
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
"""
finally 절은 예외 발생 여부와 상관없이 실행되므로,
파일이 성공적으로 열리든 아니든 반드시 파일이 닫힙니다.
이렇게 하면 자원의 누수를 방지할 수 있습니다.
"""

