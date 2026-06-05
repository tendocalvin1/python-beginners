# functions (deep dive)
# Excellent. This is actually one of the most important topics in Python.
# If dictionaries are the most important data structure, then functions are one of the most important programming concepts.
# A backend application is essentially thousands of functions working together.
# Django itself is built on functions and classes.
# AI agents are constantly calling functions (tools), processing inputs, and returning outputs.


def welcome(name):
    print(f"Welcome {name}")
    
welcome("Tendo")


def square(number):
    return number * number

print(square(5))

# Function Anatomy
def greeting(name):
    print(f"Hello {name}")
    
greeting("Daniella")

# Local Variables
# Variables inside functions

def test():
    age = 24
    print(age)
test()


def show():
    city = "Kampala"
    print(city)
show()


# Multiple Parameters
def create_user(name, country):
    print(name)
    print(country)
    
create_user("Tendo", "Uganda")

# *args
def skills(*args):
    print(args)
    
skills("Python", "Django", "Docker")


# **kwargs
def profile(**kwargs):
    print(kwargs)
    
profile(
    name  = "Tendo Calvin",
    skills =  "Data engineering"
)

# challenge 1
def show_server(server_name):
    print(server_name)
    
show_server("web-01")


# challenge 2
# def calculate_total(*numbers):
#     total = 0
    
#     for number in numbers:
#         total += number
        
# calculate_total(10, 20, 30)

numbers = [10, 20, 30]

def calculate_total(*args):
    total = 0
    for number in numbers:
        total += numbers
        return total
        
print(calculate_total())
        


# challenge 3
def show_profile(**kwargs):
    print(kwargs)
    
    
show_profile(
    name = "Tendo Dave",
    country = "Kenya"
)

