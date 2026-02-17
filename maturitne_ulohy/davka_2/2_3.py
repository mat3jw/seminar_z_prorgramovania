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
        print("subor nenajdeny")

spracuj_tricka('tshirts.txt')