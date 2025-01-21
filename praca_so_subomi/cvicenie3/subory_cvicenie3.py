dni = ["pondelok", "utorok", "streda", "stvrok", "piatok"]

#1

with open("txt1.txt", "w", encoding= "utf-8") as subor:
    subor.writelines(dni[0])

        
with open("txt1.txt", "r", encoding= "utf-8") as subor:
    print(subor.read())
    
print("====================================")

#2

with open("txt2.txt", "w", encoding= "utf-8") as subor:
    subor.writelines(dni[4])

        
with open("txt2.txt", "r", encoding= "utf-8") as subor:
    print(subor.read())

# 3

print("====================================")

with open("txt3.txt", "w", encoding= "utf-8") as subor:
    for i in dni:
        subor.writelines(i + " ")

        
with open("txt3.txt", "r", encoding= "utf-8") as subor:
    print(subor.read())
    

print("====================================")

#4

with open("txt4.txt", "w", encoding= "utf-8") as subor:
    for i in dni:
        subor.writelines(i + "\n")

        
with open("txt4.txt", "r", encoding= "utf-8") as subor:
    print(subor.read())
    
    
print("===================================")

#5
with open("txt5.txt", "w", encoding= "utf-8") as subor:
    for i in dni:
        subor.writelines(i + ", ")

        
with open("txt5.txt", "r", encoding= "utf-8") as subor:
    print(subor.read())

    

