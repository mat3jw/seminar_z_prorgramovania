from random import *
from string import *

male_pismena = ascii_lowercase

with open("log.txt") as file, open("maskovany.txt", "w") as maskovany_file:
    for riadok in file:
        riadok = riadok.strip()

        posun = randint(1, 26)

        novy_riadok = ""

        for znak in riadok:
            if znak in male_pismena:
                pozicia = male_pismena.find(znak)
                pozicia = (pozicia + posun) % 26
                novy_riadok += male_pismena[pozicia]
            else:
                novy_riadok += znak

        zakodovany_posun = male_pismena[posun - 1]
        print(zakodovany_posun, novy_riadok)
        maskovany_file.write(zakodovany_posun + novy_riadok + "\n")