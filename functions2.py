

def add(number1, number2):
    return number1 + number2


print(add(2,4))

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#          * unpacking operator
#            1. positional  2. default  3. keyword  4. arbitrary

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum(1,2,3,4,5))


def display_name(*args):
    for arg in args:
        print(arg, end= " ")
        
display_name("David", "Beckham")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
    

print_address(street = "123 Fake Street",
              city = "Detroit",
              state = "MI",
              zip = "54321"
              
              )





    