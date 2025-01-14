#cislo = int(input('zadajte cislo: '))

def delitele_cisla(cislo):
    delitele = []

    for i in range(1, cislo + 1):
        if cislo % i == 0:
            delitele.append(i)
            
    return delitele
    

print(delitele_cisla(197))