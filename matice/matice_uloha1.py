from random import *

class Matica:
    def __init__(self, r, s, prvky = None):
        self.r = r
        self.s = s


        if prvky is None:
            prvky = [0]*(r*s)

        if len(prvky) == self.r * self.s:
            self.matica = []
            for riadok in range(r):
                zaciatok = riadok * s
                koniec = zaciatok + s
                self.matica.append(prvky[zaciatok:koniec])
        else:
            raise ValueError("Nesprávny počet prvkov pre maticu.")
                   
    def vypis(self):
        for riadok in self.matica:
            for hodnota in riadok:
                print(f"{hodnota:3}", end= ' ')
            print()

    def nastav_prvok(self, i, j, hodnota):
        if not (1 <= i <= self.r and 1 <= j <= self.s):
            raise IndexError("Index mimo rozsah matice.")
        self.matica[i-1][j-1] = hodnota

    def daj_prvok(self, i, j):
        if not (1 <= i <= self.r and 1 <= j <= self.s):
            raise IndexError("Index mimo rozsah matice.")
        return self.matica[i-1][j-1]
    
    def nahodna_matica(self, min, max):
        for r in range(self.r):
            for s in range(self.s):
                self.matica[r][s] = randint(min, max)

    def scitaj(self, ina_matica):
        if self.r != ina_matica.r or self.s != ina_matica.s:
            print("Matice sa nedajú sčítať.")
            return None
                    
            nove_prvky = []
            for i in range(self.r):
                for j in range(self.s):
                    nove_prvky.append(self.matica[i][j] + ina_matica.matica[i][j])
                    
                return Matica(self.r, self.s, nove_prvky)

def main():
    matica1 = Matica(2,4,[2,7,3,7,1,-2,-9,3])
    matica1.vypis()
    print()

    matica1.nastav_prvok(1,3,2345)
    matica1.vypis()
    print()

    print("na tomto mieste je prvok: ",matica1.daj_prvok(2,4))
    print()

    matica1.nahodna_matica(-22,22)
    matica1.vypis()
    print()

    


if __name__ == "__main__":
    main()
