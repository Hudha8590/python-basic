name="Mehshan"
#Positive indexing:
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

#Negative indexing:
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[0])

#slicing:
print(name[1:3]) #eh
print(name[1:]) #ehshan
print(name[:4]) #mehs
print(name[::2])#mhhn
print(name[::-1]) #nahsheM(reverse)
print(name[1:])#remove first letter
print(name[:-1])# remove last letter

#Modifying:
name="M"+name[1:]
print(name)

#Concatenating:
a="Hello"
b="world"
full=a + b
print(full)

#f-strings:
me="hudha"
print(f"hello {me}")

#Insert mathematical expressions
print(f"5+3= {5+3}")

#Format numbers:
price=49.6789
print(f"price= {price:.2f}") ## 2 decimal places

#case methods:
name1="hudha world"
print(name1.upper())
print(name1.lower())
print(name1.title())
name2="mehshan"
print(name2.capitalize())

#check Method:
print(name2.isalpha())
print(name2.isdigit())
print(name2.isalnum())
print(name2.isalnum())
print(name2.isupper())
print(name2.islower())

#Replace/Remove:
print(name2.replace("a","e"))
name3=" Hello world "
print(name3.strip())
name4=" Hello world "
print(name4.lstrip())
print(name4.rstrip())

#Search Method:
print(name4.find("world")) 
print(name4.startswith(" He"))
print(name4.endswith("d "))

#split & join:
print(name4.split())
print(",".join(name4))

#count:
print(name4.count("o"))

