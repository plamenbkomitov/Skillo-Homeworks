def fahrenheit_to_celsius(fahrenheit):
    celsius = ((fahrenheit - 32) * 5) / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


temp_unit = str(input("Are you entering your temperature in fahrenheit or celsius? Enter 'f' or 'c': "))
temperature = int(input("Enter temperature to convert: "))
if temp_unit == 'f':
    print(fahrenheit_to_celsius(temperature))
elif temp_unit == 'c':
    print(celsius_to_fahrenheit(temperature))
