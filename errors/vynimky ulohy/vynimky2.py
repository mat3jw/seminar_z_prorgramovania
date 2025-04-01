nazov = input('zadajte nazov suboru: ')
try:
    with open(nazov) as f:
        print(f.read())

except FileNotFoundError:
    print('Subor neexistuje')

except PermissionError:
    print('Nemate prava na otvorenie suboru')

else:
    print('Subor bol uspesne otvoreny')