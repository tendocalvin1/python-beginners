# exercises on *args and **kwargs


def order_food(*args):
    print(args)
    
    
order_food("chips", "chicken", "pork", "rice")



def student(**kwargs):
    print(kwargs)
    
student(
    name ='Tendo Calvin',
    age = 24,
    country = "Uganda"
)


def student1(*args, **kwargs):
    print(args)
    print(kwargs)

student1(
    "Python",
    "Django",
    name="Tendo",
    country="Uganda"
)


def show_courses(*args):

    for course in args:
        print(course)
        
show_courses("Python","Django","PostgreSQL")
# printing the tuple : print(args) result : ("Python","Django","PostgreSQL")

# looping through the tuple: 
# for course in args:
#    print(course)

# output: 
# Python
# Django
# PostgreSQL


def show_skills(*args):
    for skill in args:
        print(skill)
    

show_skills("python", "django", "postgreSQL")   
