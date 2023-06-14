import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess number between 1 and {x}: '))
        if guess<random_number:
            print("Sorry, guess again. Too low🥴")
        elif guess>random_number:
            print("sorry, guess again. Too high🙄")
    print("Bravo! Bravo!😝, congrats😇 you have guessed the number correctly✅")
guess(20) 
