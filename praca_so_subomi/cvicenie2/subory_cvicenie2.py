from random import *

with open("ucenie_sa_slovicok.txt", encoding= "utf-8") as subor:
#1
    vsetky = subor.readlines()
    vsetky = [riadok.strip() for riadok in vsetky]
    #print(vsetky)
    
    svk = []
    svk.append(vsetky[::2])
    svk2 = [riadok for sublist in svk for riadok in sublist]
    #print(svk2)
    #print(svk)
    
    eng = []
    eng.append(vsetky[1::2])
    eng2 = [riadok for sublist in eng for riadok in sublist]
    #print(eng2)
    #print(eng)

#2
    for i in range(len(svk2)):
        print(f"{svk2[i]} = {eng2[i]}")
        
        
#3
    pozicia = randint(0, len(svk2) - 1)
    odpoved = input(f"Preloz slovo {eng2[pozicia]}:")
    if odpoved == svk2[pozicia]:
        print("spravny preklad")
    else:
        print('nespravne, spravny preklad je', svk2[pozicia])