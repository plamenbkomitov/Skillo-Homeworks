def factorial(final_number, current_number=1, current_factorial=1):
    if final_number < 0:
        return "The number you've entered is negative. Enter an integer."
    elif current_number < final_number:
        return factorial(final_number, current_number + 1, current_factorial * current_number)
    elif current_number >= final_number:
        return current_factorial * current_number


number = int(input("Enter your number: "))
print(factorial(number))
