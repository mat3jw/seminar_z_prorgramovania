class zlomok:
    def __init__(self, citatel, menovatel):
        if menovatel == 0:
            raise ValueError("Menovateľ nemôže byť nula.")
        self.citatel = citatel
        self.menovatel = menovatel
        

    def __str__(self):
        return f"{self.citatel}/{self.menovatel}"
    def daj_desatinne_cislo(self):
        return self.citatel / self.menovatel
    
    def nsd(self):
       a =self.citatel
       b =self.menovatel
       while a != b:
            if a > b:
                a -= b
            else:
                b -= a
       return a

    def daj_zmiesane_cislo(self):
        vysledok = ""
        if self.citatel // self.menovatel != 0:
         vysledok += f"{self.citatel // self.menovatel} "
        if self.citatel % self.menovatel != 0:
         vysledok += f"{self.citatel % self.menovatel}/{self.menovatel}"
        return vysledok
    
    def zakladny_tvar(self):
       delitel = self.nsd()
       novy_citatel = self.citatel // delitel
       novy_menovatel = self.menovatel // delitel

       return zlomok(novy_citatel, novy_menovatel)
    
    def __mul__(self,zlomok2):
       novy_citatel = self.citatel * zlomok2.citatel
       novy_menovatel = self.menovatel * zlomok2.menovatel

       return zlomok(novy_citatel, novy_menovatel).zakladny_tvar()
       

zlomok1 = zlomok(12, 16)
zlomok2 = zlomok(9, 3)
zlomok3 = zlomok1.zakladny_tvar()
zlomok4 = zlomok1 * zlomok2
print(zlomok4)