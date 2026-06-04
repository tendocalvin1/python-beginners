
# A string is simply text.
name = "Tendo"
country = "Uganda"
email = "tendo@gmail.com"

print(name[0])
print(country[0])
print(email[0])

print(type(name))
print(type(country))
print(type(email))

language = "python"
print(language[-1])

# string methods
print(len(language))

# string concatenation
# combining strings
first_name = "Tendo"
last_name = "Calvin"
title = "SWE"

full_name = title + " " + first_name + " " + last_name
print(full_name)

# string methods
# methods are functions attached to strings

# 1. upper()
# conerts to uppercase
name = "tendo"

print(name.upper())

# 2. lower()
name = "TENDO"

print(name.lower())


# 3. title
name = "tendo calvin"

print(name.title())


# 3. strip()
# removes spaces from both ends
name = "   Tendo   "

print(name.strip())

# 4. replace()
sentence = "I love Java"

print(sentence.replace("Java", "Python"))


framework = "Django"

print(framework.replace("Django", "FastAPI"))


email = "tendo@gmail.com"

print("@" in email)

# looping through strings
# a string is a sequence
name_one = "Tendo"

for letter in name_one:
    print(letter)
    

username = "kamara"

print(f"Welcome {username.upper()}")


character = "Danny"
for letter in character:
    print(letter)


email_address = 'danny@gmail.com'
if "@" in email_address:
    print("Valid email address")
    
else:
    print("Invalid email address")
