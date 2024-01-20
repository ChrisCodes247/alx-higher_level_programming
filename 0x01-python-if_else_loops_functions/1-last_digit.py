#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
message = f"last digit of {number} is {last_digit}"
if last_digit > 5:
    message += " and is greater than 5"
    print(message)
elif 0 < last_digit < 6:
    message += " and is less than 6 and not 0"
    print(message)
else:
    message += " and is 0"
    print(message)
