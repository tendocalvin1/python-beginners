# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
fruits = {"apple", "orange", "banana","coconut"}
print(fruits)
fruits.add('guavas')
print(fruits)
fruits.remove('orange')
print(fruits)
# fruits.pop('banana')
print(fruits)
fruits.clear()
print(fruits)