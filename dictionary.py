# a dictionary = a collection of {key: value} pairs ordered and changeable. No duplicates

capitals = {
    "Uganda": "Kampala",
    "Kenya": "Nairobi",
    "Tanzania": "Dodoma",
    "India": "New Delhi",
    "England": "London",
    "Wales": "Cardiff"
}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("Hungary"))
print(capitals.get("Uganda"))
print(capitals.get("Dodoma"))

capitals.update({"Russia": "Moscow"})
print(capitals)

capitals.update({"Russia": "St. Petersburg"})
print(capitals)

capitals.pop("Russia")
print(capitals)

capitals.popitem()
print(capitals)



keys = capitals.keys()
print(keys)

for key, value in capitals.items():
    print(f"{key} : {value}")