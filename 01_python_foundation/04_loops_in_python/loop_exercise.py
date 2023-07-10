#  Modify the code so that the "evens" list contains only the ven numbers of the "number" list.

# --- Part One ---
numbers = [1, 2, 3, 4, 5, 6, 7]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

    # --- Part Two ---
    user_input = input("Enter your choice")
    if user_input == "a":
        print("Add")
    elif user_input == "q":
        print("Quit")
