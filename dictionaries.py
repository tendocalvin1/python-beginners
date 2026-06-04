# A dictionary stores data as key --> value 
# creating a dictionary in python
student = {
    "name": "Tendo Calvin",
    "age": 21,
    "course": "computer science"
}

# Accessing values
# Here, we use the key to access the value
print(student["name"])

# adding new data
student["country"] = "Uganda"

print(student)

# updating data 
student["course"] = "Artificial Intelligence"
print(student)

# The .get() method
person = {
    "name": "Daniel Agger",
    "age" : 24
}


print(person.get("age"))


# looping through keys
person = {
    "name": "Santan Dave",
    "age": 22
}


for key in person:
    print(key)
    
# looping through values
for values in person.values():
    print(values)
    
    
# looping through key value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    
    
# membership testing 
print("name" in person)


# challenge 1
server = {
    "hostname": "web-01",
    "ip": "192.168.1.10",
    "status": "online"
}

print(server["hostname"])
print(server["status"])


# challenge 2
developer = {
    "name": "Tendo",
    "language": "Python"
}

developer["framework"] = "Django"
print(developer)


# challenge 3
cpu_stats = {
    "cpu": 70,
    "memory": 50,
    "disk": 80
}

for key, value in cpu_stats.items():
    print(f"{key}: {value}")