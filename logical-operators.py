# The and Operator
# Think of and as: "Both things must be true."

age = 24
has_id = True

print(age >= 18 and has_id)

# Truth Table for and
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# The or Operator
# Think of or as: "At least one thing must be true."

# is_admin = False
# is_owner = True

# print(is_admin or is_owner)

# Truth Table for or
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

# The not Operator
# Think of not as: "Reverse the answer."
print(not True)
print(not False)


age1 = 25
has_identity = True

if age1 >= 18 and has_identity:
    print("Entry allowed")
else:
    print("Entry denied")
    

# Systems Engineer Challenge 1
logged_in = True
account_active = True

if logged_in == True and account_active == True:
    print("Access Dashboard")
    
else:
    print("Access Denied")
    
# Systems Engineer Challenge 2
is_admin = False
email_verified = True

if is_admin == False or email_verified == True:
    print("Reset password")
    
else:
    print("Reset failed")
    
# Systems Engineer Challenge 3
verified = False

if not verified == False:
    print("Please get verification")