#polymorphism in function:
def add(a,b):
    return a+b

print(add(30,40))
print(add("sting ","join"))
print(add([1,2],[3,4]))

#polymorphism in class:(method overriding)
class Dog:
    def sound(self):
        return "bark"
    
class cat:
    def sound(self):
        return "Meow!"
 

for animal in (Dog(),cat()): #polymorphism
    print(animal.sound())
#👉 Both classes have sound(), but each gives different output.

#Polymorphism + Inheritance:
class Bird:
    def fly(self):
        print("birld can fly")

class sparrow(Bird):
    def fly(self):
        print("sparrow fly fast")

class Ostrich(Bird):
    def fly(self):
        print("ostrich can't fly")

for b in (Bird(),sparrow(),Ostrich()):
    b.fly()

#Method Overloading (Python doesn't support it):
# class Test:
#     def add(self,a):
#         print(a)

#     def add(self,a,b):
#         print(a+b)

# obj=Test()
# obj.add(5,10) # ❌ gives error because 'b' is missing

#correct way:
class Test:
    def add(self,a,b=0):
        return a+b
        
obj=Test()
print(obj.add(5))
print(obj.add(5,10))