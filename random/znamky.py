meno = input('zadajte meno ziaka: ')
predmet = input('zadajte predmet: ')
znamky = [int(znamka) for znamka in input('zadajte znamky: ').split()]
average = sum(znamky) / len(znamky)


print(meno,',', predmet,':')
for znamka in znamky:
    print(znamka, end = ', ')
    
print()

spravne_znamky = True

for i, znamka in enumerate(znamky):
    if znamka < 1 or znamka > 5:
        #print('neplatne znamky')
        spravne_znamky = False
        
if spravne_znamky:
    text_znamky = ['vyborny', 'dostatocny', 'dobry', 'dostatocny', 'nedostatocny']
    print('priemer znamok je: ', average)
    print(text_znamky[round(average) - 1])
    
else:
    print('neplatne znamky')


