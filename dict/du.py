import json

with open("mesta-sveta.json", "r", encoding= "utf-8") as file:
    mesta = json.loads(file.read())

    # pocet miest
    print(f"V JSONe je {len(mesta)} zaznamov")
    print("-" * 25)

    # pocet miest zo Slovenska
    pocet = 0
    for mesto in mesta:
        if mesto["country"] == "SK":
            pocet += 1
    print(f"Slovenskych miest je {pocet}")

    # pocet krajin
    krajiny = []
    for country in mesta:
        if country["country"] not in krajiny:
            krajiny.append(country["country"])
    print(f"Pocet krajin je {len(krajiny)}")
    print("-" * 25)

    # zistite pocet miest na severnej a na juznej pologuli
    # LATITUDE = zemepisna sirka
    # LONGITUDE = zemepisna dlzka
    S = 0
    J = 0
    for pologula in mesta:
        if pologula["coord"]["lat"] > 0:
            S += 1
        else:
            J += 1
    print(f"Pocet miest na severe je {S} a na juhu {J}")
    print("-" * 25)

    # najdite udaje o najsevernejsom a najjuznejsom meste
    najsevernejsie_mesto = mesta[0]
    najjuznejsie_mesto = mesta[0]

    for mesto in mesta:
        if mesto["coord"]["lat"] > najsevernejsie_mesto["coord"]["lat"]:
            najsevernejsie_mesto = mesto
        if mesto["coord"]["lat"] < najjuznejsie_mesto["coord"]["lat"]:
            najjuznejsie_mesto = mesto

    print(f"Najsevernejsie mesto je {najsevernejsie_mesto['name']}")
    print(f"Najjuznejsie mesto je {najjuznejsie_mesto['name']}")
    print("-" * 25)


    # zistite ktore slovenske mesto je podla udajov najzapadnejsie a najvychodnejsie
    slovenske_mesta = []

    for mesto in mesta:
        if mesto['country'] == "SK":
            slovenske_mesta.append(mesto)

    najzapadnejsie = slovenske_mesta[0]
    najvychodnejsie = slovenske_mesta[0]

    for mesto in slovenske_mesta:
            if mesto["coord"]["lon"] > najvychodnejsie["coord"]["lon"]:
                najvychodnejsie = mesto
            if mesto["coord"]["lon"] < najzapadnejsie["coord"]["lon"]:
                najzapadnejsie = mesto

    print(f"Najzapadnejsie mesto je {najzapadnejsie['name']}")
    print(f"Najvychodnejsie mesto je {najvychodnejsie['name']}")
    print("-" * 25)