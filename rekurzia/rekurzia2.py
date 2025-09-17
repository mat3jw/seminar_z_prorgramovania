def sucet_od_1_po_n(n):
    return sum(range(1, n + 1))

n = int(input("Zadaj číslo N: "))
print(f"Súčet čísel od 1 po {n} je {sucet_od_1_po_n(n)}")