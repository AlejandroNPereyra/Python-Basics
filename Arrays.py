# Suposem que hem fet una compra en un fruiteria. Les fruites i el seu import ens apareix en el tiquet de la manera següent:

# Pomes: 3,56 €
# Mandarines: 4,35 €
# Síndria: 6,23 €
# Maduixes: 4,28 €
# Peres: 2,86
# Taronges: 3,48 €
 

# Guarda la llista de la compra en forma de diccionari (pots ometre les unitats). 

purchase = dict(apple=3.56, mandarin=4.35, watermelon=6.23, strawberry=4.28, pear=2.86, orange=3.48)

# Escriu el codi per tal de resoldre les qüestions següents:

# Podries calcular la mitjana de la compra accedint als valors de les claus? Procura posar només dos decimals.

spent_in_apples = purchase['apple']
spent_in_mandarines = purchase['mandarin']
spent_in_watermelon = purchase['watermelon']
spent_in_straberries = purchase['strawberry']
spent_in_pears = purchase['pear']
spent_in_oranges = purchase['orange']
number_of_fruits = len(purchase)

total_spent_in_fruits = spent_in_apples + spent_in_mandarines + spent_in_watermelon + spent_in_straberries + spent_in_pears + spent_in_oranges
average_spent_in_fruits = round(total_spent_in_fruits / number_of_fruits ,2)
print()
print("Average spent in fruits is:", average_spent_in_fruits,"€")
print()

# Podries copiar i guardar en una nova variable la llista dels imports sense tenir en compte els dos últims?

# Obtener la lista de los importes sin los dos últimos elementos

new_purchase = list(purchase.values())[:-2]
print("Purchase without the last two items:", new_purchase)
print()

# Podries saber com comprovar si hem comprat llimones?

print ('lemon' in list(purchase))