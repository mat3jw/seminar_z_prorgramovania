cislo = int(input('zadajte cislo: '))
delitele = []

for i in range(1, cislo + 1):
    if cislo % i == 0:
        delitele.append(i)
        
print(delitele)

if len(delitele) <= 2:
    print('dane cislo je prvocislo')
    
else:
    print('dane cislo je zlozene cislo')
    