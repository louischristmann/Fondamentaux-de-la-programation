def table_de_multiplication(nombre):
    resultat_liste = []
    print("{:2f}")
    for i in range(10):
        resultat = nombre * i
        resultat_liste.append(resultat)
        print(f"{nombre} * {i} = {resultat:.1f}")
    return resultat_liste

nombre_utilisateur = float(input("Vous cherchez la table de multplication de quel nombre ?"))

resultats = table_de_multiplication(nombre_utilisateur)