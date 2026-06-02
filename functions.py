# function = A block of reusable code
# place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old!")
    print(f"Happy birthday {name}")
    
    
happy_birthday("Tendo", 24)
happy_birthday("Onana", 29)



def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("Nathan", 112.487, "02/06/2026")
display_invoice("David", 23.459, "30/06/2026")


def add(number1, number2):
    sum = number1 + number2
    return sum


def subtract(number1, number2):
    subtraction = number1 - number2
    return subtraction


def multiply(number1, number2):
    multiplication = number1 * number2
    return multiplication


def divide(number1, number2):
    division = number1 / number2
    return division


print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))


def create_name(firstname, lastname):
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    
    return firstname + " " + lastname

full_name = create_name("tendo", "calvin")
print(full_name)