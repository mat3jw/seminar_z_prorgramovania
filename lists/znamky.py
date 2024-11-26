meno = input('zadajte meno ziaka: ')
predmet = input('zadajte predmet: ')
znamky = [int(znamka) for znamka in input('zadajte znamky: ').split()]
average = sum(znamky) / len(znamky)

print(meno ,',', predmet, ':')
print(znamky)

if znamka < 0 or znamka > 6:
    print('neplatne znamky')

?

