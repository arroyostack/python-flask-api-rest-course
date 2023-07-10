friends = ["Rolf", "Jen", "Bob", "Anne"]

# print(f"{friends[0]} is my friend")
# print(f"{friends[1]} is my friend")
# print(f"{friends[2]} is my friend")
# print(f"{friends[3]} is my friend")

# Intead of repeating code with is considered a bad practice the loop is here to help
for friend in friends:
    print(f"{friend} is my mate")

# Moreover loops in python allow us to repeat the code for a specific number of times
for i in range(4):
    print(f"Hello{i}")


# Find the average grade example
grades = [35, 58, 93, 27, 40, 22, 31, 12, 21, 15, 5]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

average = total / amount
print(average)

# An alternative to the bellow code will be to simply use the python function "sum()"
alt_grades = [35, 58, 93, 27, 40, 22, 31, 12, 21, 15, 5]
alt_total = sum(alt_grades)
alt_amount = len(grades)

alt_average = alt_total / alt_amount
print(int(alt_average))
