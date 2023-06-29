# A "list" is an array like type (collection) that allow to modify add or substract elements
usersList = ["Rick", "Morty", "Summer", "Beth", "Jerry"]

# Similar to a list, "tuple" content can not be modify
usersTuple = ("Rick", "Morty", "Summer", "Beth", "Jerry")
# If you create a tuple with only one element, you need to add a coma after first elment to python interpret it as a tuple.ß

# A "set", can not have duplicate elements. Unlike tuples and lists, sets do not maintain an order
usersSet = {"Rick", "Morty", "Summer", "Beth", "Jerry"}

# You can access elements in the lists and tuples by adressing the index number. Set can not be address by index
# print(usersList)
# print(usersTuple[2])

# Add elements to the end of lists
usersList.append('Bird Person')

# Add elements to the en d of sets
usersSet.add('Mr MeeSeeks')

# Elements can not be add to tuples

# LISTS ARE MOST USED


# Advance set operations
local_friends = {"Summer", "Beth", "Jerry"}
abroad = {"Rick", "Morty"}

# Return the difference/remainder of compared sets
local_friends = {"Rick", "Morty", "Summer", "Beth", "Jerry"}
abroad = {"Rick", "Morty"}
remainder_friends = local_friends.difference(abroad)
# output >>>>>> {"Summer", "Beth", "Jerry"}

# Unites two sets togheter
local_friends = {"Summer", "Beth"}
abroad = {"Rick", "Morty"}
all_friends = local_friends.union(abroad)
# Output >>>>>> {"Rick", "Morty", "Summer", "Beth", "Jerry"}

# Interset two sets. Find elments present in both sets
friends = {"Rick", "Morty", "Mr Meeseek", "Bird Person"}
family = {"Rick", "Morty", "Summer", "Beth", "Jerry"}

firend_and_family = friends.intersection(family)

print(firend_and_family)
# output >>>>>>> {"Rick", "Morty"}
