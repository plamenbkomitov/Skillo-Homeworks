for i in range(1, 1001, 1):
    print(i, end=" ")
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    print()
