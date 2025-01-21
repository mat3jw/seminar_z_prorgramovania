meno = input("zadaj meno suboru: ")


#1
with open(meno, "r", encoding= "utf-8") as subor:
    file = subor.readlines()
    second_line = file[1]
    print("'" + second_line.strip() + "'")
    
#2
    
    
with open(meno, "r", encoding= "utf-8") as subor:
    def sirka(meno):
        riadky = subor.readlines()
        for i in riadky:
            print(len(i))
        return len(i)
            
            
#             ?????????????????????????????????????????/
            
