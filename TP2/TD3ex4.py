def factorielle_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorielle_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

def main():
    n = int(input("Entrez un entier n pour calculer la factorielle : "))

    choix_boucle = input("Choisissez la boucle (for/while) : ")

    if choix_boucle == "for":
        resultat = factorielle_for(n)
    elif choix_boucle == "while":
        resultat = factorielle_while(n)
    else:
        print("Choix de boucle invalide. Veuillez choisir 'for' ou 'while'.")
        return

    print(f"La factorielle de {n} est : {resultat}")

if __name__ == "__main__":
    main()