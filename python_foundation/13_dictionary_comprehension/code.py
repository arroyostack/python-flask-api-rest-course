# Lets convert a list of tuples into a dictionary containing tuples using comprehension.
users = [
    (0, "Rick", "password"),
    (0, "Morty", "password"),
    (0, "Summer", "password"),
    (0, "Beth", "password"),
]


user_mapping = {user[1]: user for user in users}

print(user_mapping)
# Output ==> {'Rick': (0, 'Rick', 'password'), 'Morty': (0, 'Morty', 'password'), 'Summer': (0, 'Summer', 'password'), 'Beth': (0, 'Beth', 'password')}

# Let's simulate the login of a user

username_input = input("What's you name")
user_password = input("What's you password")

_, username, password = user_mapping[username_input]

if username_input == username:
    print(f"Welcome {username}, you password is {user_password}")
else:
    pass
