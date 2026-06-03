# if statement
age = 15

if age >= 18:
    print("You are an adult")
    
print("program finished")


# The if ... else Statement
# if condition:
#     do_this
# else:
#     do_that


my_age = 16

if my_age >= 18:
    print("Adult")
    
else:
    print("Minor")
    

password_correct = True
if password_correct:
    print("Access granted")
    
else:
    print("Access denied")
    
    
# The elif Statement
# What if there are more than two possibilities ?
score = 85
if score >= 90:
    print("Grade A")

elif score >= 80:
    print("Grade B")
    
elif score >= 70:
    print("Grade C")
    
else:
    print("Grade D")
    
    
# Nested Conditionals
# You can place an if inside another if.

age1 = 24
has_id = True

if age >= 18:
    
    if has_id:
        print("Entry allowed")
        
    else:
        print("ID required")

else:
    print("Too young")
