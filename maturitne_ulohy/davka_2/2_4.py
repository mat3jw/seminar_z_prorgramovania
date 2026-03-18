def check_number(number: str):
    if len(number) != 10:
        return False
    first_9 = number[:9]
    if not first_9.isdigit():
        return False
    if number[-1] not in "123456789X":
        return False
    
    weight = 10
    suma = 0
    for digit in first_9:
        suma += weight * int(digit)
        weight -= 1
    if number[-1] == "X":
        suma += 10
    else:
        suma += int(digit)

    return suma % 11 == 0


with open("inventory.txt") as file, open("valid.txt", "w") as valid, open("invalid.txt", "w") as invalid:
    line = file.readline()
    print(line)
    numbers = line.split()
    print(len(numbers))

    for n in numbers:
        if check_number(n):
            valid.write(n + "\n")
        else:
            invalid.write(n + "\n")
