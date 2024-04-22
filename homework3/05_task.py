from random import randint

while True:
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    answer = first_number + second_number
    guess = int(input(f"How much does {first_number} + {second_number} equal to? "))
    if guess == answer:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again!")
