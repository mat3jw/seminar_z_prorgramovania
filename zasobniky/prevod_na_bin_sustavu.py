def prevod_na_binarnu(cislo):
    zasobnik = []
    binarne_cislo = ""
    aktualne_cislo = cislo
    if aktualne_cislo == 0:
        return "0"
    while aktualne_cislo > 0:
        zvysok = aktualne_cislo % 2
        #push
        zasobnik.append(str(zvysok))
        aktualne_cislo //= 2

    while not zasobnik == []:
        #pop
        binarne_cislo += zasobnik.pop()
    return binarne_cislo

print(f"Desiatkova 13 je v binarnej sustave: {prevod_na_binarnu(13)}")

        