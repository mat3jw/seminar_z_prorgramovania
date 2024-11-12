cislo = int(input("Zadajte cislo: "))

def delitelnost(cislo):
    return (True if cislo%7 == 0 else False)
    

print(delitelnost(cislo))