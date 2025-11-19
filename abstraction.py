#functional abstraction:
from abc import ABC,abstractmethod
class car(ABC):    # car is an abstract class because it has an @abstractmethod.
    @abstractmethod
    def start(self):
        pass
class BMW(car):
    def  start(self):
        print("bmw started")
class Audi(car):
    def start(self):
        print("Audi started")

obj1=BMW()
obj1.start()

obj2=Audi()
obj2.start()

#another example:
#from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print("paid by upi")
class card(payment):
    def pay(self):
        print("paid by card") 

p=UPI()
c=card()
p.pay()
c.pay()

#types of abstarction:
#data abstraction:
class student:
    def __init__(self,name):
        self.__mark=90 # private variable
        self.name=name
    def get_mark(self):
        return self.__mark # only accessible through method
std1=student("hudha")
print(std1.name)
print(std1.get_mark())


