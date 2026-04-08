def analyze_dives(filename):
    drones = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if not parts: continue
                
                name = parts[0]
                country = parts[1]
                depths = list(map(int, parts[2:]))
                drones.append({'id': name, 'country': country, 'depths': depths})

        # 1. Kontrola počiatočnej kalibrácie
        print("--- Kalibrácia (prvé 3 drony) ---")
        for drone in drones[:3]:
            print(f"{drone['id']}: {max(drone['depths'])} m")

        # 2. & 3. Zoznam krajín a distribúcia
        countries = [d['country'] for d in drones]
        unique_countries = sorted(list(set(countries)))
        print(f"\nUnikátne krajiny: {', '.join(unique_countries)}")
        
        print("\nDistribúcia výrobcov:")
        for c in unique_countries:
            print(f"{c}: {countries.count(c)}")

        # 4. Držiteľ Abyssal Record
        max_depth_overall = -1
        champions = []

        for drone in drones:
            drone_max = max(drone['depths'])
            if drone_max > max_depth_overall:
                max_depth_overall = drone_max
                champions = [drone['id']]
            elif drone_max == max_depth_overall:
                champions.append(drone['id'])

        print(f"\nAbsolútny šampión ({max_depth_overall} m): {', '.join(champions)}")

    except FileNotFoundError:
        print("Súbor dive_logs.txt nebol nájdený.")

analyze_dives('dive_logs.txt')
