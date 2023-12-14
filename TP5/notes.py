def main():
    notes = []
    coefficients = []

    for i in range(5):
        saisie = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant (séparés par un espace) : ")
        valeurs = saisie.split()
        
        if len(valeurs) != 2:
            print("Erreur : Veuillez entrer deux valeurs.")
            return
        
        note = float(valeurs[0])
        coefficient = int(valeurs[1])

        notes.append(note)
        coefficients.append(coefficient)

    moyenne = sum(note * coefficient for note, coefficient in zip(notes, coefficients)) / sum(coefficients)

    if moyenne > 10 and all(note >= 8 for note in notes):
        print(f"L'étudiant est admis avec une moyenne de {moyenne:.2f}.")
    else:
        print(f"L'étudiant n'est pas admis avec une moyenne de {moyenne:.2f}.")

if __name__ == "__main__":
    main()