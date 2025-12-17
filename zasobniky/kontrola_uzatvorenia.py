def over_uzatvorenie(vyraz):
    zasobnik = []
    pary = {')': '(', '}': '{', ']': '['}
    for znak in vyraz:
        if znak in pary.values():
            zasobnik.append(znak)
        elif znak in pary.keys():
            if not zasobnik:
                return False
            posledna_otvaracia = zasobnik.pop()
            if posledna_otvaracia != pary[znak]:
                return False
    return len(zasobnik) == 0


testy = ['([{}])', '))((', '[]]]']
for test in testy:
    vysledok = over_uzatvorenie(test)
    print(f"Vyraz {test} je spravny: {vysledok}")
        
        