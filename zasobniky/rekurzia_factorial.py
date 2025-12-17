def factorial(n):
    print(f"PUSH: volanie factorialu({n})")
    if n < 0:
        print("zadane zaporne cislo.")
        return False
    if n == 0:
        print(f"POP: ak n = 0,vratim 1")
        return 1
        
    else:
        vysledok = n * factorial(n - 1)
        print(f"POP: volanie factorialu({n}) dokoncene, vysledok {vysledok}")
        return vysledok
    
factorial(5)