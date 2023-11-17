import time

while True:
    try:
        n = int(input("Veuillez saisir un nombre entier positif : "))
        if n >= 0:
            break
        else:
            print("Veuillez entrer un nombre positif.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")


while n >= 0:
    print(n)
    time.sleep(1)
    n -= 1

