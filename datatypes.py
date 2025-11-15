# BASIC DATATYPES:
#int
x=10
print(type(x))

#float
y=3.14
print(type(y))

#complex
a=3+2j
print(type(a))

#bool
t=True
f=False
print(type(t))

#str
name="hudha"
print(type(name))

#list
fruits=["apple","orange","banana","grapes"]
print(type(fruits))
print(fruits)
fruits[1]="pappaya"
fruits.append("mango")
fruits.remove("apple")
fruits.remove(fruits[3])
print(fruits)

#tuple
tup=(1,2,3,4)
print(type(tup))

#range
ran=range(10)
print(ran) #output range(0, 10)
print(list(ran)) #output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10,2)))

#set
a={1,2,3}
print(type(a))

cars={"bmw","benz","bmw","audi"}
print(cars)
print(list(cars))
print("bmw" in cars)
#frozenset
b=frozenset({1,2,3})
print(type(b))

c=frozenset([1,2,2,4])
print(c)


#dictionary(dict)
student={
    "name":"hudha",
    "age": 22,
    "course":"python"
    }
print(type(student))
print(student["name"])
print(student["age"])
print(student["name"],student["age"])

#add to student
student["email"]="hudhathazhathayil@gmail.com"
print(student)

#removing data
student.pop("course")
print(student)
del student["age"]
print(student)

student2={
    "name":"mehshan",
    "age":21,
    "email":"mehshan@gmail.com",
    "course":"SAP",
    "degree":"BCCOM CA "
}

print(student2.keys())
print(student2.values())
print(student2.items())
student2.update({"mother":"ayisha"})
print(student2)
print(student2.pop("course"))
print(student2)
student2.clear()
print(student2)
