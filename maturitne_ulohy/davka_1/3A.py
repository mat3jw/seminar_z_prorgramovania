# Vstupný súbor log.txt obsahuje viacero riadkov (môžu obsahovať malé a veľké písmená základnej/anglickej abecedy, čísla, medzery, interpunkciu).

# Vytvorte program, ktorý:

# číta riadky zo súboru a každý riadok zároveň vypíše na obrazovku,
# šifruje iba malé písmená a–z, ostatné znaky ponechá bez zmeny,
# pre každý riadok náhodne vyberie posun k v intervale 1 až 26 a týmto posunom zašifruje všetky malé písmená v danom riadku (kruhový posun v abecede),
# do výstupu uloží každý zašifrovaný riadok tak, že na jeho začiatok pridá jeden znak, ktorý kóduje posun:
# posun 1 → a, posun 2 → b, … posun 26 → z,
# zapíše výsledok do súboru log_maskovany.txt.
# Poznámka: Dešifrovanie neriešte.

# Jedna z možných podôb výstupu pre priložený vstupný súbor:

# b2026-01-20 12:00:01 INFO  ugpuqt=ykpf urggf=5.2o/u uvcvwu=qm
# d2026-01-20 12:00:05 WARN  wirwsv=vemr zepyi=0.0qq viewsr=xmqisyx?
# f2026-01-20 12:00:12 INFO  yzgzout xkhuuz xkwakyzkj he gjsot.
# hxqvo: pwab=umbmw.twkit amy=1 bqum=12ua
# jzsxq: rycd=wodoy.vymkv coa=2 dswo=11wc
# lqddad: omzzaf abqz ruxq /hmd/pmfm/dmi.oeh (bqdyueeuaz pqzuqp)
# nbchs: qozwpfohs oh 13:30; rc bch dcksf ctt!
# pwfi vyn: bqj=48.1486N bed=17.1077E
# rtsucmh ugehdwlwv: 3 xadwk, 0 xsadwv.

import random
import string


male_pismena = string.ascii_lowercase

with open("log.txt") as file, open("log_maskovany.txt", "w") as maskovany_file:
    for riadok in file:
        riadok = riadok.strip()
        
        # vytvor nahodny posun od 1 po 26
        posun = random.randint(1, 26)
        
        novy_riadok = ""
        
        for znak in riadok:
            # ak je to male pismeno
            if znak in male_pismena:
                # zistime, na ktorom mieste je znak, pricom tu bude platit: a je na pozicii 0, b je na pozicii 1, c je na pozicii 2 ...
                pozicia = male_pismena.find(znak)
                
                # vypocitame poziciu zakodovaneho znaku - pripocitame posun a pomocou ZVYSKU pripadne vratime spat
                pozicia = (pozicia + posun) % 26
                
                # pridame zakodovany znak do noveho riadku
                novy_riadok += male_pismena[pozicia]
            else:
                novy_riadok += znak
        
        # urcime pismenko, ktore bude reprezentovat posun
        # ma platit, ze posun 1 → a, posun 2 → b, … posun 26 → z
        # to vlastne znamena, ze ak od posunu odpocitame 1, tak dostaneme index daneho znaku v abecede
        # a tuto abecedu mame v premennej "male_pismena"
        zakodovany_posun = male_pismena[posun - 1]        
        print(zakodovany_posun, novy_riadok)
        maskovany_file.write(zakodovany_posun + novy_riadok + "\n")