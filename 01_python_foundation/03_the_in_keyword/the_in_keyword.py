# We can use the "in" keyword in cases where we want to check if an element is present in a list/tuple...

# ecosystem = ["Python", "Flask", "MySQL"]

# print("Flask" in ecosystem)
# ***************************
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you have watched recently")

# print(user_movie in movies_watched)

# Using the "in" keyword in if statements

if user_movie in movies_watched:
    print(f"the movie {user_movie} wa watched by the user")
else:
    print("We have not seen this movie yet")
