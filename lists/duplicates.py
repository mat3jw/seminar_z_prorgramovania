x = input()
zoznam1 = []

for i in x.split():
    if i not in zoznam1:
        zoznam1.append(i)
        
print(zoznam1)