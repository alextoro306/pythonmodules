def vuosi(vuosiluku):

    if vuosiluku % 4 == 0:
        if vuosiluku % 100 == 0:
            if vuosiluku % 400 == 0:
                     return True
            else:
                return False
        else:
            return True
    else:
        return False

vuosiluku = int(input("Anna vuosiluku: "))

if vuosi (vuosiluku):
    print(f"{vuosiluku} on karkausvuosi")
else:
    print(f"{vuosiluku} ei ole karkausvuosi")