def est_bissextile(annee):
    # Vérifie si l'année est bissextile selon les conditions données
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(jour, mois, annee):
    # Vérifie si la date est valide
    if mois < 1 or mois > 12:
        return False
    
    jours_par_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Vérifie si l'année est bissextile et ajuste le nombre de jours de février
    if est_bissextile(annee):
        jours_par_mois[2] = 29
    
    if jour < 1 or jour > jours_par_mois[mois]:
        return False
    
    return True

def main():
    # Demande à l'utilisateur de saisir une date au format JJ/MM/AAAA
    date_saisie = input("Veuillez entrer une date au format JJ/MM/AAAA : ")
    
    # Essaye de convertir la saisie en trois entiers (jour, mois, année)
    try:
        jour, mois, annee = map(int, date_saisie.split('/'))
    except ValueError:
        print("Format de date incorrect. Veuillez entrer une date valide au format JJ/MM/AAAA.")
        return
    
    # Vérifie si la date est valide et affiche le résultat
    if est_date_valide(jour, mois, annee):
        print("La date est valide.")
    else:
        print("La date n'est pas valide. Veuillez corriger votre saisie.")

# Appel de la fonction principale
if __name__ == "__main__":
    main()
