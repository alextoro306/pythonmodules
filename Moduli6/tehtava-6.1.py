import random

def noppa():
    return random.randint(1, 6)

def main():
    while True:
        noppa1 = noppa()
        print(f"heitetään noppaa... nopan silmäluku on {noppa1}")
        if noppa1 == 6:
            break
main()