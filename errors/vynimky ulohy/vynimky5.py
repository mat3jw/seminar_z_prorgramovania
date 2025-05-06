def main():
    try:
        # Načítanie známok od používateľa
        znamky = input("Zadaj známky oddelené medzerou: ").strip()
        
        znamky_list = znamky.split()
        

        if not znamky_list:
            raise ZeroDivisionError("Chyba: Nezadal si žiadne známky!")
        
        znamky_cisla = [float(znamka) for znamka in znamky_list]
        
        priemer = sum(znamky_cisla) / len(znamky_cisla)
        print(f"Priemer známok je: {priemer:.2f}")
    
    except ValueError:
        print("Chyba: Zadal si nečíselnú hodnotu!")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()