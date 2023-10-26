nombre = float(input("Entrez un nombre : "))

positivite = "positif" if nombre > 0 else "négatif" if nombre < 0 else "zéro"
parite = "pair" if nombre % 2 == 0 else "impair"

print(f"Le nombre est {positivite} et est {parite}.")

