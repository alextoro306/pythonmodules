luku = int(input("Anna kokonaisluku: "))

def alkuluku(luku):
    if luku < 2:
        return False

    for i in range(2, luku):
        if luku % i == 0:
            return False
    
    return True

if alkuluku(luku):
    print(f"luku {luku} on alkuluku")
else:
    print(f"luku {luku} ei ole alkuluku")