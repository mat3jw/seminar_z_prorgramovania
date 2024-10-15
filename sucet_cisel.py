cislo = int(input("zadajte cislo: "))
sucet = 0
while cislo > 0:
    cislo = int(input("zadajte cislo: "))
    sucet += cislo 
    if cislo < 0:
        print(sucet - cislo)
        break
        
#opravit