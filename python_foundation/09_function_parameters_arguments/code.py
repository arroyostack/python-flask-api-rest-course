# In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.

def add(x, y):
    pass

# A function that prints two parameters added


def addition(x, y):
    result = x + y
    print(result)


addition(5, 7)


# If you pass an argument to a function that have no parameters python will thro an error

# Let's create a user greeting app

def greeting(name, surname):
    print(f"Welcome {name} {surname}")


greeting("Alayi", "Arroyo")


# In python we can change the order of arguments by naming them.

def user_profile(name, id):
    print(f"Hi {name}, you id is {id}")


user_profile(id=477837, name="Sally")

# It is recommended to use keyword arguments "named arguments" whenever possible **************
