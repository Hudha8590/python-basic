#Types:
#protected variable:
class student:
    def __init__(self):
        self._mark=90
    def get_mark(self):
        return self._mark
    
std1=student()
print(std1.get_mark())
#accessing protected variable in sub class:
class A:
    def __init__(self):
        self._name="hudha"
class B(A):
    def b(self):
        return self._name
obj1=B()
print(obj1.b())

#Private variables:
class hudha:
    def __init__(self):
        self.__mark=10
    def get_marks(self):
        return self.__mark
new=hudha()
print(new.get_marks())

#private variables is not accessible in sub classes:
class A:
    def __init__(self):
        self.__value = 100   # private

class B(A):
    def show(self):
        print(self.__value)  # ❌ ERROR

obj = B()
obj.show()
