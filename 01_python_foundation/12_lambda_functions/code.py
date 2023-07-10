# Lambda in a another type of Python function which is un-named and it's only use to return values.
# Lambda functions are exclusively used to operates on inputs and return outputs.
# Lambdas are un-names functions.
# They are usually a single line of code due to it's readability difficulty.
# Lambdas can be assigned to a variable or otherwise included into a line of code.


# This Lambda expression do not have effect in anything since is not attached to a variable.
lambda x, y: x + y

# Attached to a variable.


def add(x, y): return x + y


# Attached to int elements. Not commonly used since the code lack of readability.
(lambda x, y: x * y)(5, 7)

# Next let's create doubled numbers using first List Comprehension, then the "map" function, and finally a lambda.
sequence = [1, 3, 5, 7, 8, 2, 4, 9, 0, 2]


def double(x):
    return x * 2


# List Comprehension. Best option
doubled_list_comprehension = [double(x) for x in sequence]

# Using "map". Use if  if working with other developer/languages. Fallback is that it returns a map object instead of a list
doubled_map = list(map(double, sequence))

print(doubled_map)
