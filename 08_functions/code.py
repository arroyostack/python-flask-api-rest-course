# Let's do a hello world app
def first_function():
    print("Hello World")


first_function()


# Let's do an age to seconds calculator

def user_age_in_seconds():
    user_age = int(input("What is you age"))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(age_in_seconds)


user_age_in_seconds()


# Functions have their own scope as well as they have access to global scope variables

# Usually you want to put global variables at the top
# Notice how each time you call the function a new instance of "Rolf" is added to the set
peers = []


def add_peer():
    peers.append("Rolf")


add_peer()
add_peer()
add_peer()

print(peers)
