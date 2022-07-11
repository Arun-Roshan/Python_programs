# a program that will select a random name from a list of names. The person selected will have to pay for everybody's
# food bill.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = len(names)
p = random.randint(0, a-1)
print(f"{names[p]} is going to buy the meal today!")

