n1 = input("Merci de donner le nom de la première personne : ").upper()
p1 = input("Merci de donner le prénom de la première personne : ").capitalize()

n2 = input("Merci de donner le nom de la deuxième personne : ").upper()
p2 = input("Merci de donner le prénom de la deuxième personne : ").capitalize()

if n1 <= n2 and p1 < p2:
    print(f"personne1: {n1} {p1}")
    print(f"personne2: {n2} {p2}")
else:
    print(f"personne2: {n2} {p2}")
    print(f"personne1: {n1} {p1}")