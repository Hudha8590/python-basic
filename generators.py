# def numbers():
#     yield 1
#     yield 2
#     yield 3
# g=numbers()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) #this code will crash

def infinite_numbers():
    n=1
    while True:
        yield n
        n+=1

i=infinite_numbers()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i)) #this code will work  without crashing the memory.


def mygen():
    
       yield  n
    

m=mygen()
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))