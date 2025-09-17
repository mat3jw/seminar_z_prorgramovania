import os

cesta = "C:\\Windows"
vysledok = os.listdir(cesta)
for cosi in vysledok:
    print(cosi, os.path.isdir(cesta + "\\" + cosi))