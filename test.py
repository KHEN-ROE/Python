#Write a program that reads a positive integer
# and checks if it's a prime number using a for loop.

num = int(input("input posotive integer"))

if num < 0:
    print("양의 정수만 입력")
elif num < 2:
    print("not a prime number")
else:
    i = 2
    while True:
        if num % i == 0:
            print("not a prime num")
            break
        else:
            print("prime num")
            break
        i = i + 1


