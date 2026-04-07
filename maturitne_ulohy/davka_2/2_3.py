#Cvičenie č. 2-3: Objednávky farieb firemných tričiek so zmenami objednávok
# Súbor tshirts.txt obsahuje jeden záznam na riadok:

# ID_zamestnanca kód_farby

# Kód farby je jeden znak:

# k – čierna
# w-biela
# b-modrá
# g-sivá

# Zamestnanec môže zmeniť svoju voľbu; toto sa zobrazí ako neskorší riadok s rovnakým ID a iným kódom farby. Posledná voľba sa počíta; všetky predchádzajúce voľby sa zrušia. Vytvorte program, ktorý:

# Vypočíta celkový počet platných objednávok (po použití zmien).
# Spočíta platné objednávky pre každú farbu.
# Vypíše deduplikovaný zoznam zamestnancov (každé ID presne raz).
# Skontroluje, či má niektorá farba menej ako 15 objednávok; ak áno, vypíše kódYes farby.
# Ak každá farba spĺňa minimum 15, vypíše správu s uvedením tejto skutočnosti.
# Bonus: vypíšte, koľko zamestnancov zmenilo svoj výber aspoň raz.

def spracuj_tricka(nazov_suboru):
    objednavky = {}

    try:
        with open(nazov_suboru, 'r') as subor:
            for riadok in subor:
                casti = riadok.split()
                if len(casti) < 2:
                    continue
                
                objednavky[casti[0]] = casti[1]

        print(f"celkovy pocet platnych objednavok: {len(objednavky)}")

        farby = {'k': 0, 'w': 0, 'b': 0, 'g': 0}
        for f in objednavky.values():
            if f in farby:
                farby[f] += 1

        print(f"zoznam zamestnancov: {list(objednavky.keys())}")

        vsetky_ok = True
        for kod, pocet in farby.items():
            print(f"farba {kod}: {pocet} ks")
            if pocet < 15:
                print(f"menej ako 15 objednavok pre farbu {kod}")
                vsetky_ok = False
        
        if vsetky_ok:
            print("kazda farba ma aspon 15 objednavok")

    except FileNotFoundError:
        print("subor sa nenasiel")

spracuj_tricka('tshirts.txt')