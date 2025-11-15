#Lambda:
square=lambda x:x*x
print(square(5))

add=lambda a,b:a+b
print(add(5,6))

#using map() in lambda:
nums=[1,2,3,4]
doubled=list(map(lambda x:x*2,nums))
print(doubled)

#Using lambda with filter():
num=[1,2,3,4,5,6,7,8]
evens=list(filter(lambda x:x%2==0,num))
print(evens)

#using sort():
numbers=range(1,30)
even=list()