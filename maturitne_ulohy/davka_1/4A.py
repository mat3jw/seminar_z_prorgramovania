# Dvaja hráči si vymysleli systém kódovania správ pomocou „konzolovej tabuľky“ s 10 bunkami označenými číslicami 0–9.

# Bunka 0 reprezentuje medzeru.
# Bunky 1–9 obsahujú vždy tri znaky (posledná bunka môže mať len dva), napríklad:
 
# 0: [medzera]
# 1: C B A
# 2: F E D
# 3: I H G
# 4: L K J
# 5: O N M
# 6: R Q P
# 7: U T S
# 8: X W V
# 9: Z Y
# Kódovanie funguje takto:

# Ak je písmeno v bunke ako prvé, zapíše sa číslica raz (napr. C → 1),
# ak je druhé, číslica sa zopakuje dvakrát (B → 11),
# ak je tretie, číslica sa zopakuje trikrát (A → 111),
# medzera → 0.
# Vytvorte program, ktorý:

# načíta vetu od používateľa,
# prevedie ju na veľké písmená a vypíše,
# zakóduje ju podľa tabuľky a vypíše zakódovaný text (oddeľte kódy medzerou, aby bol výstup čitateľný),
# vypočíta a vypíše, koľkokrát bola použitá každá bunka 0–9 (počítate použitie bunky, nie počet opakovaní v rámci jedného znaku).

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