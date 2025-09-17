def NSD(x, y):
    
    if y == 0:
        return x
    else:
        return NSD(y, x % y)

#def nsn(x, y):
    
    #return abs(x * y) // gcd(x, y)

# Príklad použitia:
a = 24
b = 36
print(f"NSD({a}, {b}) = {NSD(a, b)}")
#print(f"NSN({a}, {b}) = {lcm(a, b)}")