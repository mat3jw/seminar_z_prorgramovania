from random import *

def nacitaj_otazky(subor):
    otazky = []
    with open("otazky_python.txt", encoding="utf-8") as f:
        for riadok in f:
            casti = riadok.strip().split(";")
            if len(casti) != 6:
                print("chybny riadok: ", riadok)
                continue
            otazka = {"text": casti[0],
                      "moznosti": casti[1:5],
                      "spravna": casti[5]}
            otazky.append(otazka)
    return otazky

def spusti_test(otazky, pocet):
    vybrane = sample(otazky, pocet)
    skore = 0

    for i, o in enumerate(vybrane, 1):
        print(f"\n{i}. {o["text"]}")
        for j,m in zip(["A", "B", "C", "D"], o["moznosti"]):
            print(f"{j}) {m}")
        odpoved = input("tvoja odpoved: ").upper()
        if odpoved == o["spravna"]:
            skore += 1
    return skore
def uloz_vysledok(meno, skore, celkovo):
    percenta = (skore / celkovo) * 100
    with open("kandidati_vysledky.txt", "a", encoding= "utf-8") as f:
        f.write(f"{meno};{percenta:.2f}%\n")

otazky = nacitaj_otazky("otazky_python.txt")
print("pocet otazok v databaze: ", len(otazky))
meno = input("zadaj meno: ")
pocet = int(input("kolko otazok chces v teste?: "))

skore = spusti_test(otazky, pocet)

print(f"\nskore: {skore}/{pocet}")
uloz_vysledok(meno, skore, pocet)
        