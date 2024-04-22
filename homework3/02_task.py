answer = 22
while True:
    guess = int(input("How much does 5 + 17 equal to? "))
    if guess == answer:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again!")
