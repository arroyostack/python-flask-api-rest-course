# Tuple
total = 5, 5

# Destructuring
myself, my_friend = total

print(myself)
print(my_friend)


# Destructuring a dictionary in a for loop

student_attendance = {"mike": 56, "Sally": 29, "Summer": 30}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Destructuring in tuples
person = ("Bob", "42", "Mechanic")
name, _, profession = person
# In python community convention is a good practice to mark with "_" variables that we are not going to use
print(f"{name} works as {profession}")
