
fruits=["apple","orange","mango","pineapple"]
newlist=[fruit for fruit in fruits if "apple" in fruit]
print(newlist)

even=[x for x in range(10) if x%2==0]
print(even)

square=[x*x  for x in range(10) if x%2==0]
print(square)

from functools import reduce
length=[len(fruit) for fruit in fruits]
print(length)
total= reduce(lambda a,b:a+b,length)
print(total)

#dictionary comprehension:
squares={x:x**2 for x in range(1,6)}
print(squares)

nums={x:("even" if x%2==0 else "odd") for x in range(10)}
print(nums)
