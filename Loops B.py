# Torna a fer les accions anteriors, però en lloc d’introduir els números per teclat, 
# fes-ho important el mòdul random i fent ús de la funció randint().

import random

random_list = []

print ()
print("Randomizing numbers between 1-20")
print()

for k in range(10):
    random_number = random.randint(1, 20)
    random_list.append(random_number)
    
print("Numbers in your list are: ", random_list)
print()
   
for i in range(len(random_list)):
    if random_list[i] < 10:
        random_list[i] *= 3
        
    else:
        random_list[i] *= 2
        
print("Modified number list: ", random_list)
print()

print("The first five numbers in my list are: ")
for number in random_list[:5]:
    print(number)