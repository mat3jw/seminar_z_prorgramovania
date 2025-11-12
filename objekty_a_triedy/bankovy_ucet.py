class BankovyUcet:
    def __init__(self, majitel, mena,zostatok = 0):
        self.mejitel = majitel
        self.mena = mena
        self.zostatok = zostatok
        self.transakcie = []
        

    def vklad(self, suma):
        if suma > 0:
            self.zostatok += suma
            self.transakcie.append(f"Vklad: +{suma} {self.mena}")
        else:
            print("nemozno pridat zapornu sumu.")

    def vyber(self, suma):
        if suma <= 0:
            print("nemozno vybrat zapornu sumu.")
        elif suma > self.zostatok:
            print("nedostatok prostriedkov na ucte")

        else: 
            self.zostatok -= suma
            self.transakcie.append(f"Vyber: -{suma} {self.mena}")
        
    def vypis_stav(self):
        stav_uctu = f"Zostatok: {self.zostatok} {self.mena}"
        return stav_uctu

    def prehlad(self, poslednych = 5):
        return self.transakcie[-poslednych:] if self.transakcie else []


ucet1 = BankovyUcet("Katka", "EUR")
ucet2 = BankovyUcet("Milan", "EUR", zostatok = 200)

#prvy ucet
ucet1.vklad(100)
ucet1.vyber(30)
print(ucet1.vypis_stav())
print(ucet1.prehlad(5))    

#druhy ucet
ucet2.vyber(50)
ucet2.vyber(300)
print(ucet2.prehlad(2))
