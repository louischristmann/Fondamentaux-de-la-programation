def calculer_moyenne_et_ecart():
    # Demander le nombre d'étudiants à l'utilisateur
    nombre_etudiants = int(input("Entrez le nombre d'étudiants : "))

    # Vérifier si le nombre d'étudiants est valide
    if nombre_etudiants <= 0:
        print("Le nombre d'étudiants doit être supérieur à zéro.")
        return

    # Initialiser la somme des notes
    somme_notes = 0

    # Déclaration d'une liste vide qui va contenir autant de notes que d'étudiants
    notes = []
    for i in range(nombre_etudiants):
        note = float(input(f"Entrez la note de l'étudiant {i + 1} : "))
        
        # Vérifier si la note est valide (entre 0 et 20)
        if 0 <= note <= 20:
            notes.append(note)
            somme_notes += note
        else:
            print("La note doit être entre 0 et 20. Veuillez réessayer.")
            i -= 1  # Décrémenter i pour permettre à l'utilisateur de retaper la note.

    # Calculer la moyenne
    moyenne = somme_notes / nombre_etudiants

    # Afficher la moyenne
    print(f"\nLa moyenne des étudiants est : {moyenne:.2f}")

    # Calculer et afficher l'écart par rapport à la moyenne
    print("\nÉcart par rapport à la moyenne :")
    for i, note in enumerate(notes):
        ecart = note - moyenne
        print(f"Étudiant {i + 1} : {ecart:.2f}")

# Appeler la fonction
calculer_moyenne_et_ecart()