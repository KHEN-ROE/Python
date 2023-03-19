#추상 메서드
"""
추상 클래스를 정의하는 예시
abc 모듈을 import합니다.
ABC 클래스를 상속받아 추상 클래스를 생성합니다.
추상 메서드를 정의합니다. 추상 메서드는 구현 코드가 없이 메서드 이름과 매개변수만을 가진 메서드
@abstractmethod 데코레이터를 이용해 메서드를 추상 메서드로 정의합니다.
이를 통해 하위 클래스가 해당 메서드를 구현하지 않으면 오류가 발생합니다.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_num_wheels(self):
        pass

class Car(Vehicle):
    def get_num_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_num_wheels(self):
        return 2
