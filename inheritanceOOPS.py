#Inheritance:
class car:
    def sound(self):
        print("Car is......")
class Bmw(car):
    pass
cars=Bmw()
cars.sound()

#Child adds new methods:
class Animal:
    def sound(self):
        print("animal making sound")

class Dog(Animal):
    def bark(self):
        print("Bow!")

class cat(Animal):
    def meow(self):
        print("Meow!")

d=Dog()
d.sound()
d.bark()

c=cat()
c.sound()
c.meow()

#Overriding (child modifies parent method):
class Animals:
    def walk(self):
        print("animal walk like....")

class horse(Animals):
    def walk(self):
        print("Horse walk...")

h=horse()
h.walk()

#Using constructor with inheritance:
#super():
#Passing parameters to parent constructor using super():
class person:
    def __init__(self,roll):
        self.roll=roll
        
class student(person):
    def __init__(self,name,roll):
        super().__init__(roll) #calling parent constructor
        self.name=name
student1=student("hudha",22)
print(student1.name,student1.roll)


#Calling parent class constructor using super():
class parent:
    def __init__(self):
        print("parent constructor")

class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")

child1=child()

#Calling parent method inside overridden child method:
class old:
    def show(self):
        print("parent show method")

class new(old):
    def show(self):
        super().show()
        print("child show method")

p=new()
p.show()

#Types of inheritance:
#single inheritance:
class A:
    def showA(self):
        return "A printed"

class B(A):
    def showB(self):
        return "b printed"

p=B()
print(p.showA())
print(p.showB())

#multilevel inheritance:
class a:
    def showa(self):
        return "multilevel a"
class b(a):
    def showb(self):
        return "multilevel b"
class c(b):
    def showc(self):
        return "multilevel c"

multi=c()
print(multi.showa())
print(multi.showb())
print(multi.showc())

#multiple inheritance:
class C:
    def showc(self):
        return "multiple C"
class D:
    def showd(self):
        return "multiple D"
class E(C,D):
    def showe(self):
        return "multiple E"
    
multiple=E()
print(multiple.showc())
print(multiple.showd())
print(multiple.showe())

#Hierarchial inheritance:
class F:
    def showF(self):
        return "F printed"
class G(F):
    pass
class H(F):
    pass
class I(F):
    pass

obj1=G()
obj2=H()
obj3=I()

print(obj1.showF())
print(obj2.showF())
print(obj3.showF())

#hybrid inheritance:
class J:
    def showJ(self):
        return "print J"
    
class K(J):
    def showK(self):
        return "print k"
    
class L(J):
    def showL(self):
        return "print L"
    
class M(K, L):      # hybrid (multiple + hierarchical)
    def showM(self):
        return "print M"

OBJ = M()
print(OBJ.showJ())
print(OBJ.showK())
print(OBJ.showL())
print(OBJ.showM())
