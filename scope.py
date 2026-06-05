# What is scope ? Scope is where a variable can be seen and used
# local variables
def greet():
    name = "SWE David James"
    print(name)
    
greet()


# Global variables - These are variables created outside the function.
country = "Kenya"
def show_country():
    print(country)
   
show_country()


