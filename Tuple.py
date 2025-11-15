#Tuple:
fruits=("apple","orange","mango","pineapple")
print(type(fruits))

#Accessing Tuple items:
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])  

#Updating Tuple:
new_fruits=list(fruits)
print(new_fruits)
new_fruits.append("cherry")
fruits=tuple(new_fruits)
print(fruits)

#Loops in tuple
for fruit in fruits:
    print(fruit)

#Using index:
for i in range(len(fruits)):
    print(fruits[i],i)

#count() method:
print(fruits.count("apple"))

#index() method:
print(fruits.index("cherry"))