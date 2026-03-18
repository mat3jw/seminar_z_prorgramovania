#kod kazdeho pismena alebo medzery v kodovani
kody = [
    "111", "11", "1", "222", "22", "2", "333", "33", "3", 
    "444", "44", "4", "555", "55", "5", "666", "66", "6", 
    "777", "77", "7", "888", "88", "8", "99", "9"
]
statistika = [0] * 10 
vysledok = []

veta = input("Zadaj vetu: ").upper()

for znak in veta:
    if znak == " ":
        print("0", end=" ")
        statistika[0] += 1
    elif "A" <= znak <= "Z":
        index = ord(znak) - ord("A") 
        kod = kody[index]
        vysledok.append(kod)
        statistika[int(kod[0])] += 1

print(" ".join(vysledok))


for i in range(10):
    print(f"{i}: {statistika[i]}")