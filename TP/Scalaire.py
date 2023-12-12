def calculer_produit_scalaire(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def main():
    nMax = 3
    v1 = []
    v2 = []

    # Demander à l'utilisateur d'entrer n, la taille effective des vecteurs
    n = int(input("Entrez la taille effective des vecteurs (entre 1 et {}): ".format(nMax)))

    # Vérifier que n est compris entre 1 et nMax
    while n < 1 or n > nMax:
        print("La taille doit être entre 1 et {}.".format(nMax))
        n = int(input("Quelle est la taille de vo vecteurs (entre 1 et {}): ? ".format(nMax)))

    # Demander les composantes des vecteurs v1 et v2
    for i in range(n):
        v1.append(int(input("Entrez la composante {} du vecteur v1 : ".format(i + 1))))
        v2.append(int(input("Entrez la composante {} du vecteur v2 : ".format(i + 1))))

    # Calculer le produit scalaire
    produit_scalaire = calculer_produit_scalaire(v1, v2)

    # Afficher le résultat
    print("Le produit scalaire de v1 et v2 est :", produit_scalaire)

if __name__ == "__main__":
    main()
