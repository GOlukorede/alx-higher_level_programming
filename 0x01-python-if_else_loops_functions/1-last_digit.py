#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ladig = number % -10
else:
    ladig = number % 10
if ladig > 5:
    print(f"Last digit of {number} is {ladig} and is greater than 5")
elif ladig < 6 and ladig != 0:
    print(f"Last digit of {number} is {ladig} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
