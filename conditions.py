#if else:
age=30
if age>=18 and age<25:
    print("you are an adult")
elif age<18:
    print("you are teenager")
else:
    print("nothing")


marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


#Nested if
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number or zero")

#Short-hand (one-line) if
x = 10
print("Even") if x % 2 == 0 else print("Odd")

#match case:
day = "Monday"

match day:
    case "Monday":
        print("Start of the week!")
    case "Friday":
        print("Weekend is coming!")
    case "Sunday":
        print("Relax, it’s Sunday!")
    case _:
        print("Just another day...")


#Multiple matches in one case
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It’s the weekend!")
    case _:
        print("It’s a weekday.")

#With numbers
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")

#Using Conditions in Case
#You can even use if-guards (conditions after a case):
num = 7

match num:
    case x if x > 0:
        print("Positive number")
    case x if x < 0:
        print("Negative number")
    case _:
        print("Zero")
