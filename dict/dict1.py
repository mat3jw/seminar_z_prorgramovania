text = "Dnes je utorok a v celku mrazivo. Mame dve hodiny programovania."
pocty_znakov = {}


for symbol in text:
    symbol = symbol.lower()
    if symbol in pocty_znakov:
        pocty_znakov[symbol] += 1
    else:
        pocty_znakov[symbol] = 1

print(pocty_znakov)

for key, value in pocty_znakov.items():
    print(key,value)
    
