def analyze_cluster(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines: return

            max_capacity = int(lines[0].strip())
            current_load = 0
            nodes = []
            overloaded_nodes = []
            
            first_entry = None
            last_exit = None

            for line in lines[1:]:
                parts = line.split()
                if len(parts) < 5: continue
                
                received, processed, entry_t, exit_t, alias = parts
                received, processed = int(received), int(processed)
                
                # Výpočet záťaže
                current_load = current_load + received - processed
                nodes.append(alias)
                
                if current_load > max_capacity:
                    overloaded_nodes.append(alias)
                
                if first_entry is None: first_entry = entry_t
                last_exit = exit_t

            # Výpočet času
            def to_minutes(t_str):
                h, m = map(int, t_str.split(':'))
                return h * 60 + m

            total_time = to_minutes(last_exit) - to_minutes(first_entry)
            hours, mins = divmod(total_time, 60)

            print(f"Inventár uzlov: {len(nodes)}")
            print(f"Mapa pipeline: {' '.join(nodes)}")
            print(f"Správa o kritickom preťažení: {', '.join(overloaded_nodes) if overloaded_nodes else 'Žiadne'}")
            print(f"Celkové operačné okno: {hours}h {mins}m")

    except FileNotFoundError:
        print("Súbor cluster_log.txt nebol nájdený.")

analyze_cluster('cluster_log.txt')
