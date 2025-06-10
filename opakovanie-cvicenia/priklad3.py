import random

def vygeneruj_priklady(n):
    priklady = []
    while len(priklady) < n:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        vysledok = a * b
        if vysledok <= 100:
            priklady.append((a, b, vysledok))
    return priklady

def main():
    while True:
        try:
            n = int(input("Zadajte počet príkladov (1-20): "))
            if 1 <= n <= 20:
                break
            else:
                print("Počet príkladov musí byť medzi 1 a 20.")
        except ValueError:
            print("Zadajte celé číslo.")

    priklady = vygeneruj_priklady(n)
    max_body = 2 * len(priklady)
    body = 0
    ostavajuce_priklady = priklady.copy()

    with open("nasobilka_vystup.txt", "w") as file:
        file.write("Príklady na násobenie:\n")
        for a, b, vysledok in priklady:
            file.write(f"{a} * {b} = {vysledok}\n")

    while ostavajuce_priklady:
        a, b, vysledok = ostavajuce_priklady.pop(0)
        print(f"Koľko je {a} * {b}?")
        try:
            odpoved = int(input("Vaša odpoveď: "))
        except ValueError:
            print("Zadajte celé číslo.")
            ostavajuce_priklady.append((a, b, vysledok))
            continue

        if odpoved == vysledok:
            if (a, b, vysledok) in priklady:
                body += 2
                priklady.remove((a, b, vysledok))
            else:
                body += 1
            print("Správne!")
        else:
            if (a, b, vysledok) in priklady:
                print("Nesprávne, skúste znova.")
                ostavajuce_priklady.append((a, b, vysledok))
            else:
                print(f"Nesprávne. Správna odpoveď je {vysledok}.")
    print(f"Získali ste {body} bodov z maximálnych {max_body} bodov.")

if __name__ == "__main__":
    main()