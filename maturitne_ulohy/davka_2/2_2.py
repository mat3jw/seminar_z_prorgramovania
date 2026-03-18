def spracuj_fitness():
    pocet_pobociek = 0
    suma_vsetkych = 0
    
    max_hodnota = -1
    max_pobocka = ""
    min_hodnota = float('inf')
    min_pobocka = ""
    
    rezimy = {'N': 0, 'L': 0, 'C': 0}

    try:
        with open('branches.txt', 'r', encoding='utf-8') as f:
            for riadok in f:
                casti = riadok.split()
                
                if len(casti) < 5:
                    continue

                nazov = casti[0].strip(':')
                try:
                    hodnoty = [int(casti[1]), int(casti[2]), int(casti[3])]
                    rezim = casti[4]
                except ValueError:
                    continue

                priemer_pobocky = sum(hodnoty) / 3
                print(f"pobocka: {nazov}: priemer {priemer_pobocky:.2f}")

                pocet_pobociek += 1
                suma_vsetkych += sum(hodnoty)
                
                for h in hodnoty:
                    if h > max_hodnota:
                        max_hodnota = h
                        max_pobocka = nazov
                    if h < min_hodnota:
                        min_hodnota = h
                        min_pobocka = nazov
                
                if rezim in rezimy:
                    rezimy[rezim] += 1

        print("-" * 30)
        print(f"pocet pobociek: {pocet_pobociek}")
        if pocet_pobociek > 0:
            print(f"celkovy denny priemer: {suma_vsetkych / (pocet_pobociek * 3):.2f}")
        print(f"najvyssia hodnota: {max_hodnota} ({max_pobocka})")
        print(f"najnizsia hodnota: {min_hodnota} ({min_pobocka})")
        print(f"rezimy: N={rezimy['N']}, L={rezimy['L']}, C={rezimy['C']}")

    except FileNotFoundError:
        print("subor sa nenasiel")

spracuj_fitness()