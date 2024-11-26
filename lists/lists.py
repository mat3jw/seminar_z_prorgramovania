from random import *


cisla = []

for i in range(20):
    cisla.append(randint(0, 100))
    
print(cisla)

for cislo in cisla:
    print(cislo, end = ' ')
    

print()
    
for x in range(len(cisla)):
    print(cisla[x], end = ' ')

print()
    
for a, cislo in enumerate(cisla):
    print(cislo, end = ' ')
    