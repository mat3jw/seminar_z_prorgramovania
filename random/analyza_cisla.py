# ANALYZA CISLA

n = int(input("Zadajte cislo: "))


if n % 2 == 0:
    print("cislo je parne")
elif n % 2 == 1:
    print("cislo je neparne")
    
    
if n > 0:
    print("cislo je kladne")
    
elif n < 0:
    print("cislo je zaporne")
    
else:
    print("cislo sa rovna nule")
    
if abs(n) < 10:
    print("cislo ma jednu cislicu")
    
elif abs(n) < 100:
    print("cislo ma dve cislice")
    
elif abs(n) < 1000:
    print("cislo ma tri cislice")
    
else:
    print("cislo ma viac ako tri cislice")
    
