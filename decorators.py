def calculator(fn):
    def wrapper(a,b):
        print("calculating")
        result= fn(a,b)
        print("done")
        return result
    return wrapper

@calculator
def add(a,b):
    return a+b

print(add(10,30))

@calculator
def substract(a,b):
    return a-b

print(substract(3,5))

#another example:
def calculate(fn):
    def wrapper(a,b):
        print("running:",fn.__name__)
        return fn(a,b)
    return wrapper

def my_add(a,b):
    return a+b
def my_sub(a,b):
    return a-b
my_addition=calculate(my_add)
print(my_addition(5,3))
my_substraction=calculate(my_sub)
print(my_substraction(5,3))

#Decorators with arguments:
def my_decorator(fn):
    def wrapper(*arg,**kwarg):
        print("my decorator fn running")
        return fn(*arg,**kwarg)
    return wrapper
@my_decorator
def my_aadd(a,b):
    return a+b
print(my_aadd(5,10))

@my_decorator
def greet(**data):
     return f'hello',{**data}
print(greet(name="hudha",age=21))


       