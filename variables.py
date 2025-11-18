#Global variables:
x=10 #global
def glob():
    x=5
    print("inside x:",x) #local

glob()
print("outside x:",x)

#Modifying global variables inside fn:
x=10
def change():
    global x
    x=20
    

change()
print("modified x:",x) #without the change fn it  return 10

x=10
def ins():
    x=5
    print(x)

ins()
print(x)