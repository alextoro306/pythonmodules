sukupuoli = input("Syötä biologinen sukupuolesi (nainen/mies): ").lower()
hemoglobiini = float(input("Syötä hemoglobiiniarvosi: "))
    
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini >= 117 and hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini >= 134 and hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")