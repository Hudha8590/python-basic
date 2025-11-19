fruits=["apple","orange","mango","pineapple"]
#Accessing item:
#You can access items by index (starting from 0).
print(fruits[1])
#Access a range of items (slicing):\
print(fruits[0:3])
print(fruits[:2])
print(fruits[1:])

#change items:
fruits[2]="peach"
print(fruits)
#change multiple items:
fruits[1:3]=["pappaya","grapes"]
print(fruits)

#ADD ITEM TO LIST:
fruits.append("litchi")
fruits.insert(1,"Dates")#insert item at index 1
fruits.insert(1,"Dates")
fruits.extend(["banana","greenapple"])
print(fruits)

#Remove list items:
fruits.remove("banana")# remove by value
fruits.pop(3)# remove by index
del fruits[4]# remove by index
fruits.clear()#empty the list
print(fruits)

#LOOPING LISTS:
cars=["bmw","benz","audi","rollsroyce","supra"]
for car in cars:
    print(car)

#using index:
#for loop
for i in range(len(cars)):
    print(cars[i],i)

#while loop
i=0
while i<len(cars):
    print(cars[i],i)
    i+=1 #Move to the next item in the list

#LIST COMPREHENSION 
new_list=[car for car in cars if "a" in car]
print(new_list)

new_car=[car for car in cars if "bmw" in car]
print(new_car)



#index(x)
print(cars.index("bmw"))

#count(x)
print(cars.count("bmw"))

#sort()
cars.sort()
print(cars)

#reverse()
cars.reverse()
print(cars)

#copy()
new=cars.copy()
print(new)
new.append("thar")
print(new)