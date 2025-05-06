import dis

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(dis.dis(gcd)) 
