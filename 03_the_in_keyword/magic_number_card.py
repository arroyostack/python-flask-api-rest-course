#  Ask the user to enter a number
number = 7
user_input = input("Enter 'y' if you want to play").lower()

if user_input == "y":
    user_number = int(input("Guess our number"))
    if user_number == number:
        print("You've guessed correctly :)")
    elif number - user_number in (1, -1):
        print("You were off by one")
    else:
        print("Sorry, it's wrong :()")
