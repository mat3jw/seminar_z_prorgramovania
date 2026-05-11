vstup = input('zadaj sekvenciu: acut').upper()

dna = set("ACGT")
rna = set("ACGU")
vstup_sada = set(vstup)

je_dna = len(vstup) > 0 and vstup_sada.issubset(dna)
je_rna = len(vstup) > 0 and vstup_sada.issubset(rna)

if "T" in vstup and "U" in vstup:
    je_dna = je_rna = False
if not je_rna and not je_dna:
    print("neplatna sekvencia")
else:
    typ = "DNA" if je_dna else "RNA"
    print(f"identifikovany typ: {typ}")

frekvencia = {}
for nukleotid in vstup:
    frekvencia[nukleotid] = frekvencia.get(nukleotid, 0) + 1

zoradenie = sorted(frekvencia.items(), key=lambda x: (-x[1], x[1]))
print("nukleotidy podla frekvencie: ")
for n, pocet in zoradenie:
    print(f"{n}:{pocet}x")

dna_na_rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
rna_na_dna = {"C":"G","G":"C","A":"T","U":"A"}

vysledok = ""
if typ == "DNA":
    for n in vstup:
        vysledok += dna_na_rna[n]
        print("zodpovedajuce RNA: ", vysledok)
else:
    for n in vstup:
        vysledok += rna_na_dna[n]
        print("povodna DNA: ", vysledok)