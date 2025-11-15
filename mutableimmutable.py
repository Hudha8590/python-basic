#mutable
# list:
fruits=["apple","orange","mango","pineapple","pappaya"]
print("before:",fruits)
fruits.append("peach")
print("After:",fruits)
fruits.remove(fruits[-1])
print("Removed:",fruits)

#Immutable (String):
name = "Hudha"
print("Before:", name)

name = name + " Thazhathayil"  # creates a new string
print("After:", name)

#Tuple (Immutable):
colors = ("red", "blue", "green")
# colors[0] = "yellow"  ❌ This will cause an error
