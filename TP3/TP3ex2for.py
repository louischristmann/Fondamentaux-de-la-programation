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

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
