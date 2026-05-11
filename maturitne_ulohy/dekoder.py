with open("stretnutia.txt") as f:
    for line in f:
        cislo = int(line,2)
        print(chr(cislo), end="")

# sposob ako vyriesit prvu ulohu z https://moodle4.gymcadca.eu/pluginfile.php/4150/mod_resource/content/0/Kucera%20-%20navrh%20uloh%20pre%202.%20cast%20maturitnej%20skusky.pdf