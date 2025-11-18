#Variables:
#instance variables:
class person:
    def __init__(self,name):
        self.name=name

student1=person("hudha")
print(student1.name)
#class variable(static variables):
class cars:
    wheel=4
    def __init__(self,brand):
        self.brand=brand

car1=cars("bmw")
print(car1.wheel)
print(car1.brand)
#local variables
class Cars:
    def Brand(self):
        brand="bmw"
        return(brand)
    
Car1=Cars()
print(Car1.Brand())

#Methods in class:
#instance method:
class student:
    def show(self):
        print("instance method")

#class method:
class Student:
    school="Abc school"
    @classmethod
    def show(cls):
        return cls.school

Student1=Student()
print(Student1.show())

#static method:
class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
print(Math.add(10,20))