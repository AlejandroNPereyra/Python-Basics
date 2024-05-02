# suposem que fem diverses compres a l’any, en total quatre, a una empresa proveïdora que ens ven els seus productes en dòlars. Els imports de les compres són: 356.75 $, 487.45 $, 295.83 $ i 532.00 $. Haurem de convertir el valor de dòlars a euros. 

# Part 1: Calcula i imprimeix per pantalla les dades següents:
# Suma total de les compres en euros
# Mitjana de les quatre compres en euros
# Nota: procura que la variable que necessitaràs per tenir el canvi de dòlars a euros rebi la dada a través d’una entrada per teclat.

purchase_1 = 365.75
purchase_2 = 487.45
purchase_3 = 295.83
purchase_4 = 532.00

print()
print("purchase number 1 is:", purchase_1,"$")
print("purchase number 2 is:", purchase_2,"$")
print("purchase number 3 is:", purchase_3,"$")
print("purchase number 4 is:", purchase_4,"$")
print()

total_in_dollars = purchase_1 + purchase_2 + purchase_3 + purchase_4
average_in_dollars = total_in_dollars / 4

print("total purchase in dollars is:", total_in_dollars,"$")
print("average in dollars is:", round(average_in_dollars,2),"$")
print()

dollar_to_euro_ratio = round(float(input("Enter the dollar to euro ratio:")),2)
print()

total_in_euros = total_in_dollars * dollar_to_euro_ratio
average_in_euros = average_in_dollars * dollar_to_euro_ratio

print ("total in euros is:", round(total_in_euros,2),"€")
print ("average_in_euros is:", round(average_in_euros,2),"€")
print()

# Part 2: Imagina que l’última comanda (la de 532.00 $) ha tingut un problema i només arriba el 80 % del gènere en bones condicions i, per tant, diem al proveïdor que només li pagarem el 80 % de l’import acordat prèviament.

# Calcula, ara, els mateixos resultats que en el cas anterior i imprimeix-los per pantalla.
# Podries dir quin tipus de dada (informació) és la suma total de qualsevol dels dos casos?
# Sabries canviar-la a una dada del tipus string?

print("Last purchase had a problem and provider will return the 20 percent of its value")
print()
input("Press enter to continue...")

purchase_4 = purchase_4 * 80 / 100

print()
print ("Final price for purchase 4 is:", round(purchase_4,2),"$")
print()

total_in_dollars = purchase_1 + purchase_2 + purchase_3 + purchase_4
average_in_dollars = total_in_dollars / 4

print("new total purchase in dollars is:", round(total_in_dollars,2),"$")
print("new average in dollars is:", round(average_in_dollars,2),"$")
print()

total_in_euros = total_in_dollars * dollar_to_euro_ratio
average_in_euros = average_in_dollars * dollar_to_euro_ratio

print ("new total in euros is:", round(total_in_euros,2),"€")
print ("new average_in_euros is:", round(average_in_euros,2),"€")
print()
