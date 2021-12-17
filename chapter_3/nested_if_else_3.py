# Number guessing game - Nested if else
winning_number = 26
user_input = input("guess no to win: ")
user_input = int(user_input)
if user_input == winning_number:
    print("You Win !!!")
else: # nested if else
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")

