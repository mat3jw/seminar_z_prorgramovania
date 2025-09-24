import os

def vypis_obsah(cesta: str) -> int:
    obsah_priecinka = os.listdir(cesta)
    velkost = 0


    for polozka in obsah_priecinka:
        absolutna_cesta = os.path.join(cesta, polozka)

        if os.path.isdir(absolutna_cesta):
            try:
                velkost += vypis_obsah(absolutna_cesta)
            except PermissionError:
                continue

        elif os.path.isfile(absolutna_cesta):
           velkost += os.path.getsize(absolutna_cesta)

    return velkost
        
celkova_velkost = vypis_obsah("C:/Users/VlčekMatej/Desktop/temp")
print(f"{celkova_velkost:,}B")
                       