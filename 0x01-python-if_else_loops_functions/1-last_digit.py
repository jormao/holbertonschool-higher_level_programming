#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = 1
if (number < 0):
    a = -1
last_digit = (number * a) % 10
if (number < 0):
    if (last_digit == 0):
        print("Last digit of {} is 0 and is 0".format(number))
    else:
        str = "Last digit of {} is -{} and is less than 6 and not 0"
        print(str.format(number, last_digit))
elif (number == 0):
    print("Last digit of {} is 0 and is 0".format(number))
else:
    if (last_digit == 0):
        print("Last digit of {} is 0 and is 0".format(number))
    elif (last_digit < 6):
        str = "Last digit of {} is {} and is less than 6 and not 0"
        print(str.format(number, last_digit))
    elif (last_digit > 5):
        str = "Last digit of {} is {} and is greater than 5"
        print(str.format(number, last_digit))
