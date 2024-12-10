card_number = input()
card = []

for i in card_number:
    card.append(int(i))
    
    
card_neparne = card[::2]
card_parne = card[1::2]

sucet = 0

for i in card_parne:
    x = i*2
    sucet = x - 9
    
for i in card_neparne:
    sucet += i
    
#if sucet % 10 == 0:
    
    
    


    
