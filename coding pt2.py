import random

def guess(x):
    random_number = random.radint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a my age between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess is to low. Guess again ")
        elif guess > random_number:
            print("Sorry, guess to big. Guess again ")

    print(f"woohoo, you guess the age {random_number} corectly. ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        guess = random.radint(low, high)
        feedback = input(f" Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == "H":
             high = guess - 1
        elif feedback == "L":
            low = guess + 1
    print(f"Yay! the computer guess the age, {guess} correctly! ")

computer_guess(10)        


    