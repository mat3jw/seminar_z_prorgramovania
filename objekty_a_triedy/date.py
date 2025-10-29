class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        if not self.is_valid():
            raise ValueError("neplatny datum")
    #validacia datumu   
    def is_valid(self):
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1 or self.day > self.days_in_month(self.year, self.month):
            return False
        return True
    # vypocet poctu dni v mesiaci a priestupneho roku
    @staticmethod
    def days_in_month(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 0
    #textovy zapis datumu   
    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"
    
    #porovnanie datumov
    def __eq__(self,other):
        return(self.year, self.month, self.day) == (other.year, other.month, other.day)
    
    def __lt__(self,other):
        return(self.year, self.month, self.day) < (other.year, other.month, other.day)
    
    #proces pridavania dni
    def add_day(self, n):
        day = self.day + n
        month = self.month
        year = self.year

        while True:
            dim = Date.days_in_month(year, month)
            if day <= dim:
                break
            day -= dim
            month += 1
            if month > 12:
                month = 1
                year += 1

        return Date(year, month, day)
    

#testovanie
d1 = Date(2025, 3, 22)
print(d1)

d2 = d1.add_day(222)
print(d2)

print(d1 == d2)
print(d1 < d2)

try:
    d3 = Date(2023, 2, 30)

except ValueError:
    print("tento datum nie je platny!")
