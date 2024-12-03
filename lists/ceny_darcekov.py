x = int(input())

ceny = []

for cena in input().split():
    ceny.append(int(cena))
    

spolu = sum(ceny)

for darcek in ceny:
    print(spolu - darcek)