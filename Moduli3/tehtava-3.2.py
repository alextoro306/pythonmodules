luokka = str(input("Mikä on hyttiluokkasi: "))

LUX = "LUX on parvekkeellinen hytti yläkannella."
A = "A on ikkunallinen hytti autokannen yläpuolella."
B = "B on ikkunaton hytti autokannen yläpuolella."
C = "C on ikkunaton hytti autokannen alapuolella."

if luokka == "LUX":
    print(LUX)

elif luokka == "A":
    print(A)

elif luokka == "B":
    print(B)
    
elif luokka == "C":
    print(C)
else:
    print("Virheellinen hyttiluokka")