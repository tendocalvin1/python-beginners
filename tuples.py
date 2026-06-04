

person = ("Tendo", 24)

print(type(person))

languages = ("Python", "Go", "Rust")
print(type(languages))

# Indexing with tuples
skills = ("Data Engineer", "Full-stack developer", "Digital creator")
print(skills[0])
print(skills[-1])

# length with tuples
# works the same like how it works with lists
skills = ("Python", "Django", "PostgreSQL")

print(len(skills))


# looping through tuples
countries = ("Uganda", "Kenya", "Tanzania")
for country in countries:
    print(country)
    
# membership testing in tuples
clubs = ("Arsenal", "City", "United")
print("Arsenal" in clubs)  



# tuple unpacking
person = ("Tendo", 24, "Uganda")
name, age, country = person

print(name)
print(age)
print(country)


# challenge 1
servers = ("web-server", "database-server", "cache-server")

print(servers[0])
print(servers[2]) 


# challenge 2
cpu_stats = (20, 40, 60, 80)
total = 0

for cpu_stat in cpu_stats:
    total += cpu_stat
    
print(total)


# challenge 3
developer = ("Tendo",24,"Uganda")

name, age, country = developer

print(name)
print(age)
print(country)
