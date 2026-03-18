import math

with open("voyages.txt") as file:
    for line in file:
        line = line.strip()

        x = y = z = 0
        max_depth = 0

        pocty = {"U":0, "D":0, "F":0, "B":0, "L":0, "R":0}

        for cmd in line:
            if cmd in pocty:
                pocty[cmd] += 1

                if cmd == "U":
                    z += 10
                elif cmd == "D":
                    z -= 10
                elif cmd == "F":
                    y += 10
                elif cmd == "B":
                    y -= 10
                elif cmd == "L":
                    x -= 10
                elif cmd == "R":
                    x += 10

                if z < 0:
                    max_depth = max(max_depth, -z)

        vzdialenost = math.sqrt(x**2 + y**2 + z**2)

        print("finalna pozicia : ", (x, y, z))
        print("maximalna hlbka: ", max_depth)
        print("vzdialenost od zaciatku: ", round(vzdialenost, 2))

        print("Audit:")
        for p in pocty:
            print(p, pocty[p] * 10, "m")

        if max_depth > 100:
            print("VAROVANIE: ponorka sa nachadza v hlbke s vysokym tlakom!")

        print("-" * 40)
