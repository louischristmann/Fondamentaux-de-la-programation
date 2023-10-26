minute = 0
résultat = 0

print ("saisir valeur pour minute:")
minute=int(input())

jour = (minute / 60 / 24)

print("nous sommes le {:.0f}".format(jour))