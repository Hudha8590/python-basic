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
    yield  10
    yield  20
    yield  10
    yield  20
    yield  20
    yield  20

m=mygen()
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

#COUNTER:
def Count(n):
     current=0
     while current<n:
          current+=1
          yield current

Count(5)