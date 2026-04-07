# Cvičenie č. 2-4: Kódy skladových zásob s kontrolnou číslicou
# Sklad používa 10-miestne kódy „INV-10“ s pravidlami ekvivalentnými ISBN-10:

# kód má presne 10 znakov,
# prvých 9 znakov musia byť číslice 0–9,
# posledný znak môže byť číslica 0–9 alebo X (kde X = 10),
# overenie: vypočítajte súčet (hodnota číslice × pozícia), kde pozície sa počítajú sprava doľava (posledný znak má pozíciu 1, predchádzajúci má 2, …),
# kód je platný, ak je súčet deliteľný 11.
# Program by mal:

# Prečítať kódy zo súboru inv_codes.txt (kódy sú oddelené medzerami).
# Vypísať počet kódov na overenie.
# Overiť štruktúru (dĺžka/povolené znaky) aj kontrolné pravidlo.
# Zapísať platné kódy do súboru valid_inv.txt a neplatné do súboru invalid_inv.txt.
# Vzorový vstupný súbor: inventory.txt

# Súvisiaci výstup:

# Počet kódov na overenie: 20
# Platné kódy zapísané do: valid_inv.txt
# Neplatné kódy zapísané do: invalid_inv.txt

# Pre vyššie uvedený vstup by ste mali získať nasledujúci obsah výstupného súboru:

# valid_inv.txt:
# 007462542X
# 0198526636
# 0306406152
# 0201633612
# 0131103628
# 0596007124
# 0471117099
# 123456789X
# 0000000000
# 11111111111

# invalid_inv.txt:
# 0306406153
# 0201633613
# 0131103629
# 1234567890
# 0596007125
# 007462542Y
# 047111709
# 04711170990
# 02016336A2
# 123456789x

def check_number(number: str):
    if len(number) != 10:
        return False
    first_9 = number[:9]
    if not first_9.isdigit():
        return False
    if number[-1] not in "123456789X":
        return False
    
    weight = 10
    suma = 0
    for digit in first_9:
        suma += weight * int(digit)
        weight -= 1
    if number[-1] == "X":
        suma += 10
    else:
        suma += int(digit)

    return suma % 11 == 0


with open("inventory.txt") as file, open("valid.txt", "w") as valid, open("invalid.txt", "w") as invalid:
    line = file.readline()
    print(line)
    numbers = line.split()
    print(len(numbers))

    for n in numbers:
        if check_number(n):
            valid.write(n + "\n")
        else:
            invalid.write(n + "\n")
