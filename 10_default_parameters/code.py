# When can assign default parameters in functions
# In this case if no arguments are passed an error will be thrown

def addError(x, y):
    print(x + y)


# addError()
# We can avoid this by declaring a default parameter

def add(x=0, y=0):
    print(x + y)


add()


def multiply(x=5, y=5):
    print(x * y)


multiply()

# Note: You can not specify default parameters at the beginning
# def add(x=5, y) ===> error
# Note: You can add variables a default parameters add(x=starting, y=8)
