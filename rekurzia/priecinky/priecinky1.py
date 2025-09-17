import os

def vypis_obsah(cesta, uroven=0):
    try:
        vysledok = os.listdir(cesta)
    except PermissionError:
        print(" " * (uroven * 2) + "Na tuto zlozku nemam pristup:", cesta)
        return
    for cosi in vysledok:
        absolutna_cesta = os.path.join(cesta, cosi)
        prefix = " " * (uroven * 2) + "|--- "
        print(prefix + cosi)
        if os.path.isdir(absolutna_cesta):  
            vypis_obsah(absolutna_cesta, uroven + 1)

vypis_obsah("C:\\Users\\VlčekMatej")

#def vypis_obsah(cesta):
    #vysledok = os.listdir(cesta)
    #for cosi in vysledok:
        #absolutna_cesta = os.path.join(cesta, cosi)
        #print(cosi, os.path.isdir(absolutna_cesta))
        #try:
            #if os.path.isdir(absolutna_cesta):
                #vypis_obsah(absolutna_cesta)
       # except PermissionError:
           # print("Na tuto zlozku nemam pristup:", absolutna_cesta) 
#vypis_obsah("C:\\Users\\VlčekMatej")