# DRY - Don't repeat yourself - don't repeat code again and again
# Apply DRY on number guessing game -
import random # Random Module
wining_number = random.randint(1,100)  # Using Randint function
guess = 1
game_over = False

number = int(input("Enter a number btw 1 to 100: "))

while not game_over:
    if number == wining_number:
        print(f"You win, you guess number with in {guess} time")
        game_over = True
    else:
        if number < wining_number:
            print(f"too low")
        else:
            print(f"too high")
        guess +=1
        number = int(input("guess again: "))

# Using Break Statement
# while True:
#     if number == wining_number:
#         print(f"You win, you guess number with in {guess} time")
#         break
#     else:
#         if number < wining_number:
#             print(f"too low")
#         else:
#             print(f"too high")
#         guess +=1
#         number = int(input("guess again: "))

# Using Continue Statement

# while True:
#     number = int(input("Enter a number btw 1 to 100: "))
#     if number == wining_number:
#         print(f"You win, you guess number with in {guess} time")
#         break
#     else:
#         if number < wining_number:
#             print(f"too low")
#         else:
#             print(f"too high")
#         guess +=1
#         continue
