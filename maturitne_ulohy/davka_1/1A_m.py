with open("sklenik.txt") as file:
    tabulka = []
    for riadok in file:
        riadok = riadok.strip().split()
        print(riadok)
        for i in range(len(riadok)):
            riadok[i] = int(riadok[i])
            print(riadok)
        tabulka.append(riadok)
    print(tabulka)

    print(f"pocet riadkov: {len(tabulka)}")
    print(f"pocet stlpcov: {len(tabulka[0])}")

    max_teplota = min_teplota = tabulka[0][0]
    max_pos = min_pos = (0,0)

    for r in range(len(tabulka)):
        for s in range(len(tabulka[r])):
            if tabulka[r][s] > max_teplota:
                max_teplota = tabulka[r][s]
                max_pos = (r,s)
            if tabulka[r][s] < min_teplota:
                min_teplota = tabulka[r][s]
                min_pos = (r,s)
    print(f"maximum: {max_teplota} (riadok {max_pos[0] + 1} stlpec {max_pos[1] + 1})")
    print(f"minimum: {min_teplota} (riadok {min_pos[0] + 1} stlpec {min_pos[1] + 1})")

    suma = 0
    pocet = 0

    for riadok in tabulka:
        suma += sum(riadok)
        pocet += len(riadok)
    priemer = suma/pocet
    print(f"priemer: {priemer}")

    nad_priemerom = pod_priemerom = nad_prahom = 0
    for riadok in tabulka:
        for cislo in riadok:
            if cislo > priemer:
                nad_priemerom += 1
            elif cislo < priemer:
                pod_priemerom += 1
            if cislo > priemer + 15:
                nad_prahom += 1
    print(f"nad prahom: {nad_prahom}")
    print(f"nad_priemerom: {nad_priemerom}")
    print(f"pod_priemerom: {pod_priemerom}")