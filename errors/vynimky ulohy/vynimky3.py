vek = int(input("Zadaj vek: "))

if vek < 0:
    raise ValueError("Vek nemoze byt zaporny")

else:
    print("Vek je v poriadku")
