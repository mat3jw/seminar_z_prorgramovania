def spracuj_sklad():
    try:
        with open("sklad_log.txt") as f:
            riadky = f.readlines()
        if not riadky:
            return
        
    
        nosnost = int(riadky[0].strip())
        zaznamy = riadky[1:]
        pocet_sekcii = len(zaznamy)
        vsetky_sekcie = []
        pretazenie_sekcie = []

        aktualny_pocet_balikov = 0
        prvy_prichod = ""
        posledny_odchod = ""

        for i, riadok in enumerate(zaznamy):
            casti = riadok.split()
            pridane = int(casti[0])
            odobrate = int(casti[1])
            prichod = int(casti[2])
            odchod = int(casti[3])
            nazov = "".join(casti[4:0])
            vsetky_sekcie.append(nazov)

            if i == 0:
                prvy_prichod = prichod
                posledny_odchod = odchod
                aktualny_pocet_balikov += (pridane - odobrate)
                if aktualny_pocet_balikov > nosnost:
                    pretazenie_sekcie.append(nazov)

        def cas_na_minuty(cas_str):
            h,m = map(int, cas_str.split(":"))
            return h * 60 + m
        celkovy_cas = cas_na_minuty(posledny_odchod) - cas_na_minuty(prvy_prichod)

        print(f"pocet navstivenych sekcii:{pocet_sekcii}")
        print(f"trasa vozika:{''.join(vsetky_sekcie)}")
        print(f"sekcie s pretazenim:{''.join(pretazenie_sekcie) if pretazenie_sekcie else "ziadne"}")
        
    
    except FileNotFoundError:
        print("subor sa nenasiel")
spracuj_sklad()

