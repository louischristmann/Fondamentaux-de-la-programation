def somme_entiers_naturels(N):
    somme = 0
    for i in range(N + 1):
        somme += i
    return somme

def main():
    N = int(input("Entrez la valeur de N : "))
    somme = somme_entiers_naturels(N)
    print(f"La somme des N entiers naturels de 0 à {N} est : {somme}")

    while True:
        valeur_utilisateur = int(input("Entrez une valeur (entrez 100 pour terminer) : "))
        if valeur_utilisateur == 100:
            break

    valeurs_inf_10 = 0
    valeurs_10_15 = 0
    valeurs_sup_15 = 0

    for _ in range(10):
        valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))
        while valeur < 0 or valeur > 20:
            valeur = float(input("La valeur doit être entre 0 et 20. Entrez une nouvelle valeur : "))

        if valeur < 10:
            valeurs_inf_10 += 1
        elif 10 <= valeur < 15:
            valeurs_10_15 += 1
        else:
            valeurs_sup_15 += 1

    print(f"Nombre de valeurs inférieur strictement à 10 : {valeurs_inf_10}")
    print(f"Nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 : {valeurs_10_15}")
    print(f"Nombre de valeurs supérieur ou égale à 15 : {valeurs_sup_15}")

    X = float(input("Entrez un nombre X supérieur à 1 : "))
    N = 0
    somme_cumulative = 0

    while somme_cumulative <= X:
        N += 1
        somme_cumulative += N

    print(f"Le plus grand nombre N tel que la somme des entiers de 0 à N est inférieure ou égale à {X} est : {N - 1}")

if __name__ == "__main__":
    main()
