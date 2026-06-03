# The for loop
# structure
# for item in collection:
#     do_something

skills = ["Full-stack develpoer", "Digital creator", "AI engineer"]
for skill in skills:
    print(skill)
    
laptops = ["dell", "mac book", "lenovo"]
for laptop in laptops:
    print(laptop)

# The range() Function
# Sometimes you don't have a list.
# You just want to repeat something a number of times.    
    
for age in range(10):
    print(age)
    
for x in range(1, 5):
    print(x)
    
# Accumulators
# This is one of the most important loop patterns.
numbers = [10, 20, 30]
total = 0
for number in numbers:
    total += number
    
print(total)


ages = [24, 25, 26]
sum = 0

for age in ages:
    sum += age

print(sum)


# The while Loop
# A for loop repeats over a collection.
# A while loop repeats while a condition remains True.

# structure
# while condition:
#     do_something

count = 1

while count <= 3:
    print(count)
    count += 1
    
# Systems Engineer Exercise 1
servers = ["web-server", "database-server", "cache-server"]

for server in servers:
    print(server)
    
# Systems Engineer Exercise 2
users = ["Tendo", "Maria", "Karen"]

for user in users:
    print(f"Welcome {user}")
    

# Systems Engineer Exercise 3
cpu_usages = [20, 40, 60, 80]

summation = 0

for cpu_usage in cpu_usages:
    summation += cpu_usage
    
print(summation) 