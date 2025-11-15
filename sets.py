#Set:
fruits={"apple","orange","mango","pineapple","apple"}
print(type(fruits))
print(fruits) #The order may change — sets are unordered.

#set to list
fruit=list(fruits)
print(fruit)
#list to set
fruits=set(fruit)
print(fruits)

#LOOP IN  SET:
for fruit in fruits:
    print(fruit)

for items in {"a","b","c"}:
    print(items)


#Add item in set:
fruits.add("cherry")
print(fruits)

#Add multiple items at once
fruits.update(["litchi","peach"])
print(fruits)


#Remove set items:
#remove()
fruits.remove("pineapple") #  ❌ Error if item not found
print(fruits)

#discard()
fruits.discard("pineapple") # ✅ No error if item not found
print(fruits)

#pop()
x=fruits.pop()  # Removes a random item
print(x)
print(fruits)

#copy()
fruit=fruits.copy()
print(fruit)
fruit.add("mango")
print(fruit)

#clear()
fruits.clear()  # Empties the set
print(fruits)