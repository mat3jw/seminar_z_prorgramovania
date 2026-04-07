# Cvičenie č. 2-1: Harmonogram prezentácií a priradenie témy na seminár
# Na seminári je X prezentujúcich a organizátor pripravil Y tém (každá téma môže byť použitá maximálne raz). Program by mal:

# Prečítať X (počet prezentujúcich) a Y (počet tém). Ak Y ≤ X, upozorniť používateľa, že nie je dostatok tém.
# Vytvoriť náhodné poradie prezentujúcich (sú očíslovaní od 1 do X).
# Priradiť každému prezentujúcemu jedinečnú náhodnú tému (témy sú očíslované od 1 do Y); žiadna téma nemôže byť priradená viac ako raz.
# Pridajte toto obmedzenie: pretože podobné témy sa môžu prekrývať, musia sa striedať párne a nepárne témy. Dvaja po sebe idúci prezentujúci nesmú dostať obaja párnu tému ani obaja nepárnu tému.
# Výstup: zoznam v poradí prezentácie, napr. k. prezentujúci: <id>, téma: <číslo>.

# Ukážka interakcie:

# Zadajte počet prezentujúcich: 8
# Zadajte počet tém: 20
# Poradie prezentácií a priradené témy:
# 1. prezentujúci: 4, téma: 12
# 2. prezentujúci: 1, téma: 5
# 3. prezentujúci: 7, téma: 18
# 4. prezentujúci: 2, téma: 3
# 5. prezentujúci: 6, téma: 14
# 6. prezentujúci: 8, téma: 9
# 7. prezentujúci: 3, téma: 20
# 8. prezentujúci: 5, téma: 7



from random import *


x = int(input("zadajte pocet prezentujucich: "))
y = int(input("zadajte pocet tem: "))

if x > y:
    print("nie je dostatok tem pre vsetkych prezentujucich")

prezentujuci = list(range(1, x + 1))
shuffle(prezentujuci)

temy = list(range(1, y + 1))

parne = [t for t in temy if t % 2 == 0]
neparne = [t for t in temy if t % 2 != 0]

shuffle(parne) and shuffle(neparne)

priradene_temy = []
zacni_parnou = choice([True, False])

for i in range(x):
    if zacni_parnou:
        if parne:
            priradene_temy.append(parne.pop())
        else:
            priradene_temy.append(neparne.pop())
    else:
        if neparne:
            priradene_temy.append(neparne.pop())
        else:
            priradene_temy.append(parne.pop())

    zacni_parnou = not zacni_parnou

print("Poradie prezentacii a priradene temy: ")
for j in range(x):
    print(f"{j+1}. prezentujuci: {prezentujuci[j]}, tema: {priradene_temy[j]}")





    
    
