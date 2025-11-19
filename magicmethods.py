#dunder methods:
#1. __init__ → Constructor:
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Aisha")
print(p.name)

#2. __str__ → String representation:
class Person1:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person Name: {self.name}"

p = Person1("Aisha")
print(p)

#3. __len__ → Length of object:
class fruits:
    def __init__(self,items):
        self.items=items
    def __len__(self):
        return len(self.items)
fruit=fruits(["apple","mango"])
print(len(fruit))