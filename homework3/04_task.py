from random import randint
random_number = randint(1,100)

while True:
    guess = int(input("Guess the number: "))
    if guess > random_number:
        print("Too high. Try again!")
    elif guess < random_number:
        print("Too low. Try again!")
    else:
        print("Correct!")
        break
