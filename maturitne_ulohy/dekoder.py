with open("stretnutia.txt") as f:
    for line in f:
        cislo = int(line,2)
        print(chr(cislo), end="")