# Genera una seqüència iterable formada per una llista de 10 números enters majors que 0 i menors que 20. 
# Procura que tots els números d’aquesta llista els entris per teclat. 
# Una vegada tinguis la llista, realitza les accions següents:

# Fes que tots els elements siguin multiplicats per 3, si són menors que 10, o per 2, si són majors que 10. Fes ús de l’estructura for.
# Imprimeix la llista. Fes ús de l’estructura for.
# A continuació, imprimeix només els cinc primers números. Fes ús de l’estructura while.

number_list = []

print ()
print("Please enter 10 numbers between 1-20:")
print()

while len(number_list) < 10:
    number = int(input(f"Enter number {len(number_list) + 1}: "))
    print()
    if 1 <= number <= 20:
        number_list.append(number)
    else:
        print("Invalid number. Please enter a number between 1-20.")
        print()

print("Numbers in your list are: ", number_list)
print()
   
for i in range(len(number_list)):
    if number_list[i] < 10:
        number_list[i] *= 3
        
    else:
        number_list[i] *= 2
        
print("Modified number list: ", number_list)
print()

print("The first five numbers in my list are: ")
for number in number_list[:5]:
    print(number)