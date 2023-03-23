#메서드 오버라이딩
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

# 메서드 오버라이딩을 이용한 다형성 구현
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() # 각 객체에 따라 다른 동작을 수행

#메서드오버라이딩 - 사칙연산
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

class AdvancedCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

c = Calculator()
print(c.add(2, 3))        # 5
print(c.subtract(5, 1))   # 4
print(c.multiply(4, 6))   # 24
print(c.divide(10, 2))    # 5.0

ac = AdvancedCalculator()
print(ac.divide(10, 0))   # Cannot divide by zero
print(ac.divide(10, 2))   # 5.0