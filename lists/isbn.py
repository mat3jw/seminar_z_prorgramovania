isbn = input("zadajte ISBN: ")


def check_isbn(isbn):
    
    isbn = isbn.replace("-", "").replace('ISBN', "")
#print(isbn)

    cisla = list(isbn)
    cisla.remove(' ')

#print(cisla)
    neparne = cisla[1::2]
    for i in range(len(neparne)):
        neparne[i] = int(neparne[i])
    
#print(sum(neparne*3))


    parne = cisla[::2]
    for k in range(len(parne)):
        parne[k] = int(parne[k])
    
    
#print(sum(parne))
    
    sucet = (sum((neparne*3) + parne))     
    print(sucet)



    if sucet % 10 == 0:
        print('ISBN je PLATNE')
    
    else:
        print("ISBN je NEPLATNE")
#print(isbn)
#print(cisla)

check_isbn(isbn)

