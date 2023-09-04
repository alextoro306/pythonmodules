import random

def noppa(max):
    return random.randint(1, max)
max = int(input("Anna nopan max silmäluku: "))

while True:
    noppa1 = noppa(max)
    print(f"heitetään noppaa... nopan silmäluku on {noppa1}")
    if noppa1 == max:
        break