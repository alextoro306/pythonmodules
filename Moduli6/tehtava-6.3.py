def main():
    while True:
        gallona = float(input("Anna gallonamäärä: "))
        litra = gallona * 3.785
        if gallona > -1:
            print(f"{litra} litraa")
        else:
            print("Ohjelma loppuu...")
        break
main()