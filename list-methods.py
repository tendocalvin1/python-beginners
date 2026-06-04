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