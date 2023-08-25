while True:

    tuuma = int(input("Anna tuumat (Jos tuuma määrä on negatiivinen ohjelma päättyy): "))

    if tuuma < 0:
        print("Ohjelma päättyy.")
        break

    senttimetrit = tuuma * 2.54
    print(f"{tuuma} tuuma on {senttimetrit:.2f} senttimetriä")