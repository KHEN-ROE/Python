#클래스 연습문제
"""
Deposit 클래스를 생성하라.
이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
인스턴스 메소드 profit()은 n년 후 원리금을 반환한다.
n년 후 원리금은 initial * (1 + interest)n이다.
Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라.
단 원리금은 정수로 표시되어야 한다.
"""
"""
class Deposit:
    
    #생성자
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
    

    #인스턴스 메서드
    def profit(self):
        total = self.initial * (1+ self.interest)**self.n
        return int(total)
        
#인스턴스 생성
deposit1 = Deposit(1000000, 0.035, 7)
print(deposit1.profit())
"""

"""
예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고
부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 없다.
이용할 수 없다면 그 이유는? 캡슐화 돼있어서
이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가? People 클래스에 게터와 세터 메소드 생성
"""
"""
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        
    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().set_age(age)
        super().set_name(name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school, )
        print("age is", super().get_age())
        print("name is", super().get_name())
     
#인스턴스 생성     
t = Teacher(28, "noh", "dau")
t.showSchool()
"""

"""
다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
getID() 메소드는 employeeID를 반환하는 메소드이다.
Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력.
"""
class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 
    
    def getAge(self): 
        print(self.age) 

class Employee(Person):
    #생성자
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.__employeeID = employeeID
    
    #게터,세터 메소드
    def get_employeeID(self):
        return self.__employeeID
    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID
    
    def info(self):
        super().getName()
        super().getAge()
       #print(e.get_employeeID()) #이렇게 해도 되긴함...
       #print(self.__employeeID) #이거도 됨
        print("ID : ", Employee.get_employeeID(self) )
        
        
    
#인스턴스 생성
e = Employee("동양", 65, 2019)
#메소드 호출 
e.info()

