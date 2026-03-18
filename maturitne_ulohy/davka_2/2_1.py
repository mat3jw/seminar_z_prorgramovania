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





    
    
