import random

def ustne_skusanie(pocet_ziakov, pocet_otazok):
    if pocet_ziakov > pocet_otazok:
        print('Chyba: Pocet ziakov musi byt mensi alebo rovny poctu otazok.')
        return
    
#nahodne poradie studentov
    ziaci = list(range(1, pocet_ziakov + 1))
    random.shuffle(ziaci)

    #nahodne poradie otazok
    otazky = list(range(1, pocet_otazok + 1))
    random.shuffle(otazky)

#zamadzenia striedania parnych a neparnych otazok
    striedajuce_otazky = []
    parne_otazky = [otazka for otazka in otazky if otazka % 2 == 0]
    neparne_otazky = [otazka for otazka in otazky if otazka % 2 != 0]

    while parne_otazky or neparne_otazky:
        if parne_otazky:
            striedajuce_otazky.append(parne_otazky.pop(0))
        if neparne_otazky:
            striedajuce_otazky.append(neparne_otazky.pop(0))

#pridelenie otazok ziakom
    ziak_otazka = list(zip(ziaci, striedajuce_otazky[ :pocet_ziakov]))

    print("Pridelene otazky:")
    for ziak, otazka in ziak_otazka:
        print(f"Ziak {ziak} ma otazku {otazka}")

#TESTOVANIE PROGRAMU
 #nastavenie poctu otazoka a ziakov
pocet_ziakov = 30
pocet_otazok = 20
ustne_skusanie(pocet_ziakov, pocet_otazok)


