# Slicing as a method used in lists for python programming
# basic slice
# syntax: list[start:stop]

# important rule:
# start is included
# stop is excluded

skills = ["Python", "Django", "PostgreSQL", "Docker"]

print(skills[0:2])

skills = ["Python", "Django", "PostgreSQL", "Docker"]

print(skills[2:]) # output : ['PostgreSQL', 'Docker']
print(skills[-2:])

# copying a list
skills = ["Python", "Django", "PostgreSQL"]

copy = skills[:]

print(copy)

# step slicing
# list[start:stop:step]
numbers = [1,2,3,4,5,6]

print(numbers[::2])

numbers = [1,2,3,4,5,6]

print(numbers[1::2])


# insert at a specific position
skills = ["full-stack developer", "Data engineer", "digital creator"]
skills.insert(0, "ML engineer")
print(skills)


# pop - Removes an item by position
channels = ["aftv", "DR sports", "That's Football"]
removed = channels.pop()
print(removed)
print(channels)

numbers = [10,20,30]

removed = numbers.pop(1)

print(removed)
print(numbers)


# sort() - This organises a list
numbers = [5,1,2,9]
numbers.sort()
print(numbers)


# reverse() - Reverse the list in place
numbers = [1,2,3]
numbers.reverse()
print(numbers)


skills = ["Python", "Django", "Docker"]

skills.reverse()

print(skills)


# nested lists
# A list can contain other lists

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix[0]) # result = list that has numbers 1 and 2
print(matrix[0][1])  # result = number 2


# challenge 1
logs = ["info", "warning", "error", "critical"]
print(logs[2:])


# challenge 2
servers = ["web-1", "web-2", "db-1", "cache-1"]
servers.reverse()

print(servers)


# challenge 3
cpu_usages = [90, 50, 20, 70]
cpu_usages.sort()

print(cpu_usages)


# challenge 4
frameworks = ["Django", "FastAPI"]
frameworks.insert(1, "Flask")

print(frameworks)


servers = ["web", "database", "cache"]

for index, server in enumerate(servers):
    print(index, server)