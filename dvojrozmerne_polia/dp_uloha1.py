# sachovnica s numerickymi kodmi: kladne = biele, zaporne = cierne
# 1 = pesiak, 2 = jazdec, 3 = strelec, 4 = veza, 5 = kralovna, 6 = kral
sachovnica = [
        [-4,-2,-3,-5,-6,-3,-2,-4],
        [-1,-1,-1,-1,-1,-1,-1,-1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [4,2,3,5,6,3,2,4],
       ]

def zobraz_sachovnicu(sachovnica):
    sirka = 3
    for riadok in sachovnica:
        for cislo in riadok:
            print(f"{cislo:{sirka}}", end= " ")
        print()
    print()

#prvok v pravom hornom rohu
print(sachovnica[0][7])
print()

#zmena 5. prvku v 3. riadku na 100
sachovnica[2][4] = 100
zobraz_sachovnicu(sachovnica)

#vypis 7. riadku
print(*sachovnica[6])
print()

#vymena hodnoty 2. a 4. riadku
sachovnica[1], sachovnica[3] = sachovnica[3], sachovnica[1]
zobraz_sachovnicu(sachovnica)

#pridanie noveho riadku
sachovnica.append([9,9,9,9,9,9,9,9])
zobraz_sachovnicu(sachovnica)

#vlozenie riadku medzi 2. a 3. riadok
sachovnica.insert(2, [-9,-9,-9,-9,-9,-9,-9,-9])
zobraz_sachovnicu(sachovnica)