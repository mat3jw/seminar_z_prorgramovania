zoznam = []

#push
def pridaj(zoznam,prvok):
    zoznam.append(prvok)
    return zoznam
#pop
def odober(zoznam):
    zoznam.pop()
    return zoznam

def je_prazdny(zoznam):
    if len(zoznam) == 0:
        return True
#peek
def peek(zoznam):
    if not je_prazdny(zoznam):
        return zoznam[-1]
    