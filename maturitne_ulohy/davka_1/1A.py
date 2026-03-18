
mriezka = []
with open("sklenik.txt", "r") as f:
    for riadok in f:
        cisla = [int(x) for x in riadok.split()]
        if cisla:
            mriezka.append(cisla)

r = len(mriezka)
c = len(mriezka[0])
print(f"pocet riadkov: {r}")
print(f"pocet stlpcov: {c}")


minimum = mriezka[0][0]
pos_min = (1, 1)
maximum = mriezka[0][0]
pos_max = (1, 1)
suma = 0

for i in range(r):
    for j in range(c):
        hodnota = mriezka[i][j]
        suma += hodnota
        
        if hodnota < minimum:
            minimum = hodnota
            pos_min = (i + 1, j + 1)
            
        if hodnota > maximum:
            maximum = hodnota
            pos_max = (i + 1, j + 1)

priemer = suma / (r * c)

nad_priemerom = 0
pod_priemerom = 0
kriticke_miesta = 0  

for riadok in mriezka:
    for hodnota in riadok:
        if hodnota > priemer:
            nad_priemerom += 1
        elif hodnota < priemer:
            pod_priemerom += 1
            
        if hodnota >= priemer + 15:
            kriticke_miesta += 1

print(f"nad priemerom: {nad_priemerom}")
print(f"pod priemerom: {pod_priemerom}")
print(f"kriticke miesta: {kriticke_miesta}")
print(f"minimum: {minimum} (riadok {pos_min[0]}, stlpec {pos_min[1]})")
print(f"maximum: {maximum} (riadok {pos_max[0]}, stlpec {pos_max[1]})")
print(f"priemer: {priemer:.2f}")


prah = int(input("zadaj prahovu teplotu (v desatinach): "))
nad_prahom = 0
for riadok in mriezka:
    for h in riadok:
        if h > prah:
            nad_prahom += 1
print(f"nad prahom {prah}: {nad_prahom}")

