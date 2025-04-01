ovocie = ['jablko', 'banán', 'pomaranč']

print("Zoznam ovocia:", ovocie)

try:
    index = int(input("Zadaj index prvku, ktorý chceš zobraziť: "))
    print("Prvok na zadanom indexe je:", ovocie[index])

except ValueError:
    print("Chyba: Zadaná hodnota nie je číslo!")

except IndexError:
    print("Chyba: Zadaný index je mimo rozsahu zoznamu!")