#클래스와 인스턴스
class Rectangle:
    #클래스 변수 
    count=0
    
    #생성자
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #인스턴스 생성 시 클래스 변수 값 증가
        Rectangle.count +=1
    
    #메소드
    def area(self):
        return self.width * self. height

#인스턴스 생성
rectangle1 = Rectangle(3,4)
print(rectangle1.width)
print(rectangle1.height)
print(rectangle1.area())

#인스턴스 변수 값 변경
rectangle1.width = 5
print(rectangle1.width)

#인스턴스 변수 - 인스턴스 변수(Instance Variable)는 클래스의 인스턴스(객체)마다 독립적으로 사용되는 변수입니다.
#클래스 변수 - 클래스 변수(Class Variable)는 클래스의 모든 인스턴스(객체)에서 공유되는 변수. 자바의 필드와 비슷한듯 

#인스턴스 생성 시 클래스 변수 값 증가
rectangle2 = Rectangle(5,6)
print(f"count : {Rectangle.count}")

#인스턴스 메서드 - 인스턴스를 통해 호출되는 메서드
#첫 번째 인자로 self받음. self는 인스턴스 자신을 지칭. self 통해 인스턴스 변수에 접근
class bicycle:
    #생성자
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed
    
    #인스턴스 메서드
    def speedUp(self, increment):
        self.speed += increment
        
    #인스턴스 메서드2
    def brake(self, decrement):
        self.speed -= decrement

#인스턴스 생성
bike = bicycle(6,0)
#인스턴스 변수 호출
print(f"speed : {bike.speed}")
#인스턴스 메서드 호출하고 매개변수 전달
bike.speedUp(3)
print(bike.speed)
bike.brake(1)
print(bike.speed)

#클래스 메서드 - 클래스 레벨에서 동작(클래스 내부에서 쓸 목적). 클래스 변수에 접근하기 위해 사용되는 메서드
#인스턴스 메서드와의 차이 - 첫 번째 인자 cls. 클래스 변수에 대한 접근 및 수정이 가능
#인스턴스 변수에 대한 접근 불가. 따라서 클래스 메서드는 클래스 이름 이용해서 직접 호출.
class Rectangle:
    count = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
    
    @classmethod
    def printCount(cls):
        print(cls.count)
        
#클래스 메서드 호출 - 실행결과 0. 아직 인스턴스를 생성하지 않았으므로       
Rectangle.printCount()
#인스턴스 생성
rectangle1 = Rectangle(7,8)
#클래스 메서드 다시 호출 - 결과 값 1
Rectangle.printCount()

#계산기 클래스
class Calculator:
    #클래스 변수
    operator = '+'
    
    #생성자 - 정의하지 않아도 된다. 이러면 기본 생성자가 정의됨. 자바처럼
    
    #클래스 메서드
    @classmethod
    def setOperator(cls, newOperator):
        cls.operator = newOperator #위에 클래스 변수에 매개변수로 받은 값 저장
    
    #인스턴스 메서드 
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1+num2
        if Calculator.operator == '-':
            return num1 - num2
        if Calculator.operator == '*':
            return num1 * num2
        if Calculator.operator == '/':
            return num1 / num2
        
#인스턴스 생성. 생성자 없으므로 매개변수 없다 
calculator1 = Calculator()
#인스턴스 메서드 호출하고 매개변수 전달
print(calculator1.calculate(8,4))
#클래스 메서드 호출하고 매개변수 전달
Calculator.setOperator('*')
#다시 인스턴스 메서드 호출하고 매개변수 전달
print(calculator1.calculate(8,4))


#캡슐화
#java의 private과 같다
class person:
    def __init__(self, name, age):
        self.__name = name # 인스턴스의 변수를 비공개로 설정.
        self.__age = age # 인스턴스의 변수를 비공개로 설정.
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
#인스턴스 생성
person1 = person("ken", 28)
#get 메소드 호출
print(person1.get_name())
#set 메소드로 변수 값 변경
person1.set_name("kim")
#다시 get 메소드 호출
print(person1.get_name())

#상속
class People:
    #생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print("안녕하세요 제 이름은", self.name, "입니다.")
        print("나이는", self.age, "입니다.")
        
class Teacher(People): #()안에 상속받을 부모클래스 입력
    #생성자
    def __init__(self, name, age, subject):
        super().__init__(name, age) #부모 클래스의 생성자 호출
        self.subject = subject
    
    def showInfo(self):
        super().introduce()
        print("전공은", self.subject,"입니다")
        
#인스턴스 생성
t = Teacher("ken", 28, "경제학")
#인스턴스 메소드 호출 
t.showInfo()

#다중상속
class Parent1:
    def method1(self):
        print("Parent1's method1")

class Parent2:
    def method2(self):
        print("Parent2's method2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Parent1's method1
c.method2()  # Parent2's method2


