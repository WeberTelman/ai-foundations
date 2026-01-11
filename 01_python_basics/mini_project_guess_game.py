# A simple guessing game
# This teaches how AI systems loop, test, and decide

secret_number = 7
guess = None

print("Guess the secret number between 1 and 10")

while guess != secret_number:
    guess = int(input("Your guess: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct! You found it.")
