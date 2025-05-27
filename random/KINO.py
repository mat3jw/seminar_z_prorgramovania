# KINO

vek = int(input("Zadaj svoj vek: "))
cas = int(input("Zadaj cas filmu (v hodinach): "))

if vek < 1 or cas > 24 or cas < 1:
    print("chyba!")

elif (vek < 18) and (cas < 18):
    print("Cena listka je 5 eur")
    
    
elif (vek < 18) and (cas >= 18):
    print("Cena listka je 8 eur")
    
elif (vek >= 18) and (cas < 18):
    print("Cena listka je 10 eur")
    
elif (vek >= 18) and (cas >= 18):
    print("Cena listka je 12 eur")
    
    

    

   
