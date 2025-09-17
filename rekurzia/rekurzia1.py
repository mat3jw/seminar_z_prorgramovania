def mocnina(x: float, n: int) -> float:
    if n == 0:
        return 1
    else:
        return x * mocnina(x, n - 1)
    

print(mocnina(2, 3))  # 8