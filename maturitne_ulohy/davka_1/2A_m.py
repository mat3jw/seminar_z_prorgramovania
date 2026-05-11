import random
import string

with open("dobrovolnici.txt") as file, open("neplatne.txt", "w") as neplatne_file, open("registracia.csv", "w") as registracia_file:
    platne = neplatne = 0
    riadkov = 0

    dobrovolnici = []

    for riadok in file:
        riadkov += 1
        casti_mena = riadok.strip().split()
        print(casti_mena)

        if len(casti_mena) < 2:
            neplatne_file.write(f"{riadok}")
            neplatne += 1
            continue

        platne += 1
        priezvisko = casti_mena[-1]
        prve_meno = ""
        for meno in casti_mena:
            if meno not in("Ing.", "Mgr.", "Bc."):
                prve_meno = meno
                break
        print(prve_meno, priezvisko)
        id_dobrovolnika = priezvisko.lower() + "." + prve_meno.lower()

        poradie = 1
        while id_dobrovolnika in dobrovolnici:
            if id_dobrovolnika + str(poradie) not in dobrovolnici:
                id_dobrovolnika = id_dobrovolnika + str(poradie)
                break
            else:
                poradie += 1
        dobrovolnici.append(id_dobrovolnika)

        pin = ""
        for i in range(6):
            pin += str(random.randint(0,9))
    
        znaky = string.ascii_letters + string.digits + "#$%&+"
        heslo = ""
        for i in range(12):
            heslo += random.choice(znaky)

        registracia_file.write(f"{id_dobrovolnika};{pin};{heslo};{riadok.strip()}\n")