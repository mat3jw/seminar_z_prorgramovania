#1
kluce = ['Desať', 'Dvadsať', 'Tridsať']
hodnoty = [10, 20, 30]


vysledok = dict(zip(kluce, hodnoty))
print(vysledok)

#2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)


