from time import sleep
pocet_sekund = 1

spravne_heslo = 123
heslo = int(input("zadajte heslo: "))
pokus = 0
pocet_pokusov = 5

#zistovanie hesla
while True:
    if heslo != spravne_heslo:
        pokus = pokus + 1
        print("nespravne heslo, skuste to znova!")
        print("ostava ", pocet_pokusov - pokus, "pokusov")
        sleep(pocet_sekund)
        pocet_sekund = pocet_sekund * 2
        if pokus == 5:
            print("Účet zablokovaný!")
            break
        heslo = int(input("zadajte heslo: "))
    else:
        print("heslo je spravne!")
        break

