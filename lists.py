skills = ["Python", "Django"]

print(type(skills))

skills = ["Python", "Django", "PostgreSQL"]

print(skills[0])
print(skills[1])
print(skills[2])
print(skills[-1])
print(len(skills))


frameworks = ["Django", "FastAPI", "Flask"]

print(frameworks[-1])
print(frameworks[-2])

# changing items
# lists are mutable. This means that they can be modified

expertise = ["Python", "Django", "PostgreSQL"]

expertise[1] = "FastAPI"

print(expertise)

# adding items - we use append()
stuff = ["Python", "Django"]
stuff.append("PostgreSQL")
print(stuff)


# remove items - we use remove()
stuff = ["Python", "Django", "PostgreSQL"]

stuff.remove("Django")

print(stuff)


# member testing in lists. This is similar to what we did in lists
skills = ["Python", "Django", "PostgreSQL"]

print("Python" in skills)
print("Java" in skills)

# looping through lists. This is a very common pattern
skills = ["Python", "Django", "PostgreSQL"]

for skill in skills:
    print(skill)
    
names = ["Tendo", "Daniella", "Tobias"]

for name in names:
    print(name)
    

numbers = [10, 20, 30]
total = 0

for number in numbers:
    total += number
    
print(f"The sum of these numbers is {total}")


# number 1
servers = ["web", "database", "cache"]

servers.remove("database")
print(servers)

#number 2
frameworks = ["Django", "FastAPI"]

frameworks.append("Flask")
print(frameworks)


# number 3
users = ["Tendo", "Maria", "Karen"]
for user in users:
    print(user)
    
    
# number 4
cpu_usages = [10, 20, 30, 40]
total = 0

for cpu_usage in cpu_usages:
    total += cpu_usage
    
print(f"The total cpu usage is {total}")


