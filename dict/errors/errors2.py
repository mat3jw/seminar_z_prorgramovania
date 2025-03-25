# Program by mal otvorit a nacitat textovy subor,
# nasledne zistit 
#  1. frekvenciu vyskytu slov - bez rozlisovania velkosti pismen,
#  2. frekvenciu vyskytu akychkolvek znakov - opat bez rozlisovania velkosti pismen

def count_words_symbols(file_path):
    word_freq = {}
    symbol_freq = {}
 
    file = open(file_path, 'r')
    text = file.read()
    file.close()
 
    # Zmen text na male pismena
    text.lower()
 
    words = text.split(' ')
    for word in words:
        if word.isalpha():
            if word in word_freq:
                word_freq[word] =+ 1
            else:
                word_freq[word] == 1
        else:
            for char in word:
                if not char.isalnum():
                    if char in symbol_freq:
                        symbol_freq[char] += 1
                    else:
                        symbol_freq[char] = 1
 
    return word_freq, symbol_freq
 
 
file_path = 'example.txt'
print(count_words_symbols(file_path))