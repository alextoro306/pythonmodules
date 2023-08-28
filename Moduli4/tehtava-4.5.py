yritykset = 0

while yritykset < 5:

    tunnus = input("Anna käyttäjätunnus: ")
    salis = input("Anna salasana: ")

    tunnus1 = "python"
    salis1 = "rules"

    if tunnus == tunnus1 and salis == salis1:
        print("Tervetuloa")
    else:
        yritykset += 1
        print("Pääsy evätty")