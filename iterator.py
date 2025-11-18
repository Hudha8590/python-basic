nums=[10,20,30,40]
it=iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Creating Your Own Iterator:
class counter:
    def __init__(self,n):
         self.n=n
         self.current=0
    
    def __iter__(self):
         return self
    def __next__(self):
         if self.current<self.n:
              self.current +=1
              return self.current
         else:
              raise StopIteration
            
c=counter(3)
for i in c:
     print(i)