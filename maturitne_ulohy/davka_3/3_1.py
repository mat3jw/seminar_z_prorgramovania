def analyze_expressions(filename):
    empty_lines = 0
    correct = 0
    too_many_open = 0
    too_many_closed = 0

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    empty_lines += 1
                    continue

                balance = 0
                is_valid = True
                for char in line:
                    if char == '(':
                        balance += 1
                    elif char == ')':
                        balance -= 1
                    
                    # Ak klesne pod 0, zátvorka bola zatvorená skôr, než sa otvorila
                    if balance < 0:
                        is_valid = False
                
                if is_valid and balance == 0:
                    print(f"OK: {line}")
                    correct += 1
                elif balance > 0:
                    print(f"Chyba (veľa otváracích): {line}")
                    too_many_open += 1
                else:
                    print(f"Chyba (veľa zatváracích/zlé poradie): {line}")
                    too_many_closed += 1

        print("\n--- Štatistiky ---")
        print(f"Prázdne riadky: {empty_lines}")
        print(f"Správne výrazy: {correct}")
        print(f"Príliš veľa otváracích: {too_many_open}")
        print(f"Príliš málo otváracích (veľa zatváracích): {too_many_closed}")

    except FileNotFoundError:
        print(f"Súbor {filename} nebol nájdený.")

analyze_expressions('expressions1.txt')
