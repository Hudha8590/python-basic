#Recursion:
def factiorial(n):
    if n==1 : # base case
        return 1
    return n* factiorial(n-1)    # recursive call
print(factiorial(5))

#Fibonacci using Recursion:
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))