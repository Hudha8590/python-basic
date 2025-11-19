#Dictionary:
student={
    "name":"hudha",
    "age":20,
    "course":"python",
    "institute":"Bridgeon"
}
print(type(student))

#Accessing dictionary items:
print(student["name"])
print(student.get("age"))
#If the key doesn’t exist:
print(student.get("xyz")) #✅ Returns None
#print(student["xyz"]) #❌ Error

#CHANGE OR ADD new key value pair:
student["age"]=21
student["city"]="Kozhikode"
print(student)

#Remove dictionary items:
#pop(key):
student.pop("course")
print(student)
#popitem()
student.popitem()
print(student)

#del
del student["institute"]
print(student)

#clear()
student.clear()
print(student)

student2={
    "name":"Mehshan",
    "age":21,
    "course":"SAP",
    "institute":"Catalyst"
}

#LOOP THROUGH DICTIONARY:
for key in student2: # prints keys
    print(key)

for value in student2.values(): # prints values
    print(value)

for key,value in student2.items(): # prints both
    print(key,":",value)

#Nested dictionaries:
students = {
    "student1": {"name": "Aisha", "age": 20},
    "student2": {"name": "Rahul", "age": 22}
}
print(students["student1"]["name"])   # Aisha
print(students.get("student1"))
print(students.get("student1", {}).get("name"))

#Dictionary comprehension:
even={x:x*2 for x in range(1,30) if x%2==0 }
print(even)

square={x: x*x for x in range(1,6) }
print(square)

fruits=["apple","pineapple","pappaya","cherry"]
lengths={fruit:len(fruit) for fruit in fruits}
dic={i:fruit for i,fruit in enumerate(fruits)}
print(dic)
print(lengths)

#Convert two lists into a dictionary
keys = ["name", "age", "city"]
values = ["Aisha", 20, "Kochi"]
result={k:v for k,v in zip(keys,values)}
print(result)