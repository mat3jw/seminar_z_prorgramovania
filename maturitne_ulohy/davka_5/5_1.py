def nsd(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

print(nsd(453543453, 464646))