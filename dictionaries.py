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
    
    
    
# Nested dictionaries
# accessing nested data
user = {
    "name": "Tendo",
    "address": {
        "city": "Kampala",
        "country": "Uganda"
    }
}

print(user["address"]["city"])
print (user["address"]["country"])


developer1 = {
    "name": "Tendo Calvin",
    "skills" : ["Data engineer", "full-stack engineer", "digital creator"]
}

print(developer1["skills"][1])


# challenge 4
server = {
    "hostname": "web-01",
    "specs": {
        "cpu": 8,
        "memory": 32
    }
}


print(server["specs"]["cpu"])
print(server["specs"]["memory"])

# challenge 5
developer = {
    "name": "Tendo",
    "skills": [
        "Python",
        "Django",
        "PostgreSQL"
    ]
}


print(developer["skills"][0])
print(developer["skills"][1])



# advanced dictionary skills
# keys()
user = {
    "name": "Tendo",
    "country": "Uganda"
}

print(user.keys())

# values() returns all values
print(user.values())


# items()
# returns key value pairs
for key, value in user.items():
    print(key, value)


# safe access with .get()
user = {
    "name": "Tendo"
}

user.get("age")

request_data = {
    "username": "Tendo",
    "email": "tendo@gmail.com"
}

username = request_data.get("username")
email = request_data.get("email")

print(username)
print(email)