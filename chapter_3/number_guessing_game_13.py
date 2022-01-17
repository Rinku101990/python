# NUMBER GUESSING GAME

wining_number = 55
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
            guess +=1
            number = int(input("guess again: "))
        else:
            print(f"too high")
            guess +=1
            number = int(input("guess again: "))
