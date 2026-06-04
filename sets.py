
# adding items
frameworks = {
    "Django",
    "FastAPI"
}

frameworks.add("Flask")
print(frameworks)


# remove items 
frameworks = {
    "Django",
    "FastAPI",
    "Flask"
}

frameworks.remove("Flask")
print(frameworks)


# creation of unique tags 
tags = ["python","django","python","backend","django"]

unique_tags = set(tags)
print(unique_tags)

# looping through sets
skills = {"data engineer", "backend engineer", "digital creator"}

for skill in skills:
    print(skill)
    
# NB: Sets cannot be indexed since they are unordered
#     Sets cannot have duplicates in them


# challenge 2
frameworks = {"Django", "FastAPI"}
frameworks.add("Flask")
print(frameworks)


# challenge 3
emails = ["a@gmail.com","b@gmail.com","a@gmail.com","c@gmail.com","b@gmail.com"]

unique_emails = set(emails)
print(unique_emails)

# The important question
# answer: I would store them in a set because as we have discussed earlier, a set eliminates all duplicates in any given form of data.