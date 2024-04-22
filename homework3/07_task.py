import math
number = int(input("Enter your number: "))

for i in range(2, int(math.sqrt(number)) + 1, 1):
    if number != i and number % i == 0:
        print("Number is not prime.")
        break
else:
    if number < 2:
        print("Number is not prime.")
    else:
        print("Number is prime.")
