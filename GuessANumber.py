import random

random_number = random.randint(1, 10)

print()
your_number = int(input("Choose a number between 1-10:"))
print()

if random_number > your_number:
    print("the number you chose :", your_number, " is lower than the number the machine thought :", random_number)
elif random_number < your_number:
    print("the number you chose : ", your_number, " is higher than the number the machine thought :", random_number)
else:
    print("The random number: ", random_number, " is equal to the chosen number: ", your_number)