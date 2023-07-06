# functions has a special object called "args" who collects all
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(4, 3, 6, 7, 8))

# Let's create anoter function that calls multiply with arguments and an operator


def apply(*args, operator):
    if operator == "*":
        multiply(*args)
    elif operator == "+":
        add(args)
    else:
        return "No valid operator entered"


print(apply(1, 2, 3, 4, 5, operator="*"))

# The following function is invoking passing the variable nums as parameter x and y


def add(x, y):
    return x + y


nums = [3, 4]
print(add(*nums))

# If we were to assing a named arguments from a dictionary we can also use the start symbol. The following two stars will assign name argument to add

numDict = {"x": 15, "y": 25}

print(add(numDict["x"], numDict["y"]))
# We can simplify this by:
print(add(**numDict))

#
