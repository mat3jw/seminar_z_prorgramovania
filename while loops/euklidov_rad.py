n1 = int(input("zadajte prve cislo: "))
n2 = int(input("zadajte druhe  cislo: "))


while n1 != n2:
    if n1 > n2:
        n1 -= n2
        
    else:
        n2 -= n1
        

    
print(n1)