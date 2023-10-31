#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ladig = number % -10
else:
    ladig = number % 10
if ladig > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, ladig))
elif ladig < 6 and ladig != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, ladig))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
