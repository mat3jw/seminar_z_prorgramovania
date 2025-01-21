with open("udaje.txt", encoding= "utf-8") as subor:
    
    #1
    jeden_riadok = subor.readline()
    print(jeden_riadok)
    
    #2
    for riadok in subor:
        print(int(riadok))
        
    #3
    obsah = subor.read()
    print(obsah)
    
    #4
    print(subor.readlines())
    
    #5
    for riadky in subor:
        subor.seek(1)
        riadky = len(subor.readlines())
        print(riadky)
        