# List Comprehesion
# Allow to create new lists from existing lists.
# numbers = [3, 5, 7]
# doubled = []

# To end up with an array containing the doubles of the numbers aray normally this is done
# for number in numbers:
#     doubled.apeend(number * 2)

# Making use of List Comprehension we can simplify the code
numbers = [3, 5, 7]
doubled = [x * 2 for x in numbers]

print(doubled)

# In the example below the list "double" is an array that enclose a for loop iterating through the list "numbers"

# The following is an example of another time in which List Comprehension become handy.
# Let say we want to create a new list containing names starting with "s".
friends = ["Sally", "Molly", "Bret", "Santy", "Melly"]
start_s = []

# Let's compare between a solution made by a for loop vs using List comprehension
for friend in friends:
    if friend.lower().startswith("s"):
        start_s.append(friend)

print(start_s)

# Now using list comprehension with conditional
# Remember. When you create a List Comprehension a new list in created.

start_m = [friend for friend in friends if friend.lower().startswith('m')]


# If you were to compare two elements to check if they take the same place in memory you can make use of the "id()" function.

print(id(friends), id(start_m))

# This will return the id address in memory of the element.
