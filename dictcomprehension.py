#1. Create a dictionary of numbers and their squares.:
square={x:x*x for x in range(6)}
print(square)

#2. Convert a list of fruits into a dictionary where key = fruit, value = length of fruit:
fruits=["apple", "banana", "kiwi"]
lengths={fruit:len(fruit) for fruit in fruits }
print(lengths)

#Create a dictionary where keys = numbers and values = "even" or "odd":
numbers={x:("even" if x%2==0 else "odd") for x in range(8)}
print(numbers)

#4. Convert two lists into a dictionary using comprehension:
keys = ["name", "age", "city"]
values = ["Aisha", 20, "Kochi"]
dic={keys[i]:values[i] for i in range(len(keys)) }
print(dic)
#uning zip()
result={k:v for k,v in zip(keys,values)}
print(result)

#5. Create a dictionary of fruits with index as key (using enumerate):
lis=["apple", "banana", "cherry"]
index={i:fruit for i,fruit in enumerate(lis)}
print(index)

#6. Filter dictionary to only include items where value > 10:
data={"a":2,"b":12,"c":22,"d":9}
filtered={k:v for k,v in data.items() if v>10}
print(filtered)
#9. Nested dictionary comprehension:
new={ x: { "square": x*x, "cube": x*x*x } for x in range(1, 6) }
print(new)