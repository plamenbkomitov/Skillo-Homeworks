def simple_calculator(first_number, second_number, operator):
    if operator == '+':
        return first_number+second_number
    elif operator == '-':
        return first_number-second_number
    elif operator == '*':
        return first_number*second_number
    elif operator == '/':
        return first_number/second_number


print(simple_calculator(26, 0, '*'))

