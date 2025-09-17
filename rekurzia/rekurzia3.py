def sucet_cifier(x):
    if x == 0:
        return 0
    else:
        return x % 10 + sucet_cifier(x // 10)

# Príklad použitia:
cislo = 23
print(sucet_cifier(cislo))  # Výstup: 15