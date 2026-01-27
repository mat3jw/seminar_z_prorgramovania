import random
import string

def generuj_heslo():
    znaky = string.ascii_letters + string.digits + "#$%&+"
    return "".join(random.choice(znaky) for _ in range(12))

vsetky_id = []
platne_zaznamy = 0
neplatne_zaznamy = 0

with open("dobrovolnici.txt", "r") as f_in, \
     open("neplatne.txt", "w") as f_bad, \
     open("registracia.csv", "w") as f_csv:

    f_csv.write("id;pin;heslo;Povodny riadok\n")

    for riadok in f_in:
        povodny = riadok.strip()
        slova = povodny.split()

        if len(slova) < 2:
            f_bad.write(povodny + "\n")
            neplatne_zaznamy += 1
            continue

        platne_zaznamy += 1
        meno = slova[0].lower()
        priezvisko = slova[-1].lower()
        zaklad_id = f"{priezvisko}.{meno}"

        pocet_rovnakych = vsetky_id.count(zaklad_id)
        if pocet_rovnakych == 0:
            final_id = zaklad_id
        else:
            final_id = f"{zaklad_id}{pocet_rovnakych + 1}"
        
        vsetky_id.append(zaklad_id) 

        pin = f"{random.randint(0, 999999):06d}"
        heslo = generuj_heslo()

        # Zápis do CSV
        f_csv.write(f"{final_id};{pin};{heslo};{povodny}\n")

print(f"Spracovaných riadkov: {platne_zaznamy + neplatne_zaznamy}")
print(f"Platné: {platne_zaznamy}, Neplatné: {neplatne_zaznamy}")