#examples:
#1.
num=None
try:
   num=10/0
except:
  print("not divisible")
else:
   print("divisible")

print(num)

#2.
try:
   alp=int("abc")
except ValueError:
   print("Error:Not an integer")
else:
   print("integer")
   
#3.
try:
    num = int(input("Enter a number: "))   # may cause ValueError
    result = 100 / num                     # may cause ZeroDivisionError
    print("Result =", result)

except ValueError:
    print("Error: Please enter a valid integer!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


