#for loop:
#Looping through a list:
fruits=["apple","banana","mango","orange","pineapple"]
for fruit in fruits:
    print(fruit)

# #Using range():
for i in range(5):
    print(i)

# #With step:
for i in range(0,10,2):
    print(i)

# #while loop:
count=1
while count<=5:
    print("count:",count)
    count +=1

# #LOOP CONTROL STATEMENT:
# #break:
for i in range(1,10):
    if i==5:
        break
    print(i)# this will only print upto 5
    
#continue:
for i in range(1,10):
    if i==3:
        continue
    print(i)#in this it will skip the 3 from the numbers

cars=["audi","benz","bmw","minicooper"]
for car in cars:
    if car=="bmw":
        pass # does nothing, used to fill empty blocks
    print(car)