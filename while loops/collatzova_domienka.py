from time import sleep

a = int(input("zadajte cislo: "))

    
while True:
    if a % 2 == 0:
        a = a/2
        print(a)
        sleep(0.25)
    elif a % 2 == 1:
         a = (3*a) + 1
         print(a)
         sleep(0.25)
    
    if a == 1:
        print("cislo je 1")
        break
    
        