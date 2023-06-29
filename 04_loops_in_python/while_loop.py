number = 7

while True:
    user_input = input("Do you want to play? (Y/n)").lower()

    if user_input == "n":
        break

    user_number = int(input("Guess a number"))

    if user_number == number:
        print("********************")
        print("You have guessed correcly")
        print("********************")
    elif abs(number - user_number) == 1:
        print("*****************")
        print(" you were off by one")
        print("*****************")
    else:
        print("Sorry, you've got it wrong")
