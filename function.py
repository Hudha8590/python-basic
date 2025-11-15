#function:
def greet():
    print("hello")

greet() # hello

#with Arguments:
def sum(a,b):
    print(a+b)

sum(5,3) # 8
#sum(5) #error

#Arbitrary Arguments -*arg
def total(*number):
    print(number)

total(1,2,3,4,5,6,7)

def sum_all(*number):
    s=0
    for n in number:
        s +=n
        print(s)

sum_all(1,2,3,4,5)

#Keyword Arguments:
def keyword(name,age):
    print(name,age)
keyword(name="hudha",age=22)
keyword(age=21,name="mehshan",) #Order doesn’t matter when using keyword arguments.