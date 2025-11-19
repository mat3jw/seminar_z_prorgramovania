import random

class Matica:
    def __init__(self, riadky, stlpce, vypln=0):
        self.riadky = riadky
        self.stlpce = stlpce
        # vytvorenie dvojrozmerneho zoznamu (matice)
        self.data = [[vypln for _ in range(stlpce)] for _ in range(riadky)]

    def _over_index(self, i, j):
        if not (0 <= i < self.riadky and 0 <= j < self.stlpce):
            raise IndexError(f"Index out of range: ({i}, {j})")

    def nastav_prvok(self, i, j, hodnota):
        self._over_index(i, j)
        self.data[i][j] = hodnota

    def daj_prvok(self, i, j):
        self._over_index(i, j)
        return self.data[i][j]

    def nahodna_matica(self, min, max):
        for i in range(self.riadky):
            for j in range(self.stlpce):
                self.data[i][j] = random.randint(min, max)

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in riadok) for riadok in self.data)


if __name__ == "__main__":
    #pouzitie
    m = Matica(3, 4)           
    m.nahodna_matica(1, 10)    
    print("Po naplnení náhodnými číslami:")
    print(m)
    m.nastav_prvok(1, 2, 99)   
    print("\nPo zmene jedného prvku:")
    print(m)
    print("\nHodnota na (1,2):", m.daj_prvok(1, 2))
