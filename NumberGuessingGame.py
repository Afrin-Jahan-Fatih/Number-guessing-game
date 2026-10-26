# Number gussing game

import random
attempts =7

def game_rules():
    print("\n\nWelcome to Number Gussing Game \nI have selected a number between 1 and 100 \nGuess the number in 7 attempts\n\n\n")


def play_game(number, attempt=1):
    if attempt>attempts:
        print(f"\nGame Over!!! \nThe correct number was {number}\n\n")
        return

    guess = input(f"Attempt {attempt}/7 .... Enter your guess :  ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number\n")
        return play_game(number, attempt)
    if guess<1 or guess>100:
        print("Please enter a number between 1 and 100\n")
        return play_game(number, attempt)
    if guess<number:
        print("Too Low")
    elif guess>number:
        print("Too High")
    else:
        print("\n\nCongratulations!!! You guessed the correct number\nYou guessed it in",attempt,"attempt(s).")
        return
    play_game(number, attempt+1)



number = random.randint(1,100)
game_rules()
play_game(number)