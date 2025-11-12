matica = [
    [6, 9, 1, 4, 5],
    [-10, 9, 8, -3, 0],
    [100, 6, -200, 3, 7]
    ]

def zobraz_maticu(matica):
    sirka = 4
    for riadok in matica:
        for cislo in riadok:
            print(f"{cislo:{sirka}}", end= " ")
        print()
    print()

zobraz_maticu(matica)

matica[1][2] = 11
zobraz_maticu(matica)
matica.append([2, 1, 9, 2, 7])
zobraz_maticu(matica)
matica.insert(1, [5,4,3,2,1])
zobraz_maticu(matica)

del matica[3]
zobraz_maticu(matica)
