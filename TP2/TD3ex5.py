def calculer_prix_location(heure_debut, heure_fin):
    if heure_debut < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return None

    if heure_debut == heure_fin:
        print("Attention ! l'heure de fin est identique à l'heure de début.\n")
        return None

    if heure_debut > heure_fin:
        print("Attention ! le début de la location est après la fin.\n")
        return None

    if 0 <= heure_debut < 7 or 17 <= heure_debut <= 24:
        tarif = 1
    else:
        tarif = 2

    heures_location = heure_fin - heure_debut
    prix_total = tarif * heures_location

    return prix_total

while True:
    try:
        heure_debut = int(input("Veuillez entrer l'heure de début de la location (entre 0 et 24) : "))
        heure_fin = int(input("Veuillez entrer l'heure de fin de la location (entre 0 et 24) : "))
        
        prix_location = calculer_prix_location(heure_debut, heure_fin)

        if prix_location is not None:
            print(f"Le coût de la location est de {prix_location} euros.")
    except ValueError:
        print("Veuillez entrer des entiers valides pour les heures.\n")
while True:
    try:
        heure_debut = int(input("Veuillez entrer l'heure de début de la location (entre 0 et 24) : "))
        heure_fin = int(input("Veuillez entrer l'heure de fin de la location (entre 0 et 24) : "))
        
        prix_location = calculer_prix_location(heure_debut, heure_fin)

        if prix_location is not None:
            print(f"Le coût de la location est de {prix_location} euros.")
            break 
    except ValueError:
        print("Veuillez entrer des entiers valides pour les heures.\n")
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur.")
        break  