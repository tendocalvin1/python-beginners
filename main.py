# collection = single "variable" used to store multiple values
# list  = [] ordered and changeable collection, duplicates okay
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# tuple = () ordered and unchangeable collection, duplicates okay

fruits = ["apple", "orange", "banana","coconut"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[:1]) # prints out the first item in the list
# print(fruits[0:3]) # prints out the first to the third item in the list
# fruits[0] = "jack fruit"


# for fruit in fruits:
#     print(fruit)

fruits.append('guavas')
print(fruits)
fruits.remove('orange')
print(fruits)

# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.clear()
# print(fruits)
# print(fruits)

print(fruits.count("apple"))

