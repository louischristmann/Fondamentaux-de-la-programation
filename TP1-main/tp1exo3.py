jour = 0
heure = 0
minute = 0
résultat = 0

print ("saisir valeur pour jour:")
jour=int(input())

print ("saisir valeur pour heure:")
heure=int(input())

print ("saisir valeur pour minute:")
minute=int(input())

résulat=minute + (heure * 60) + (jour * 60 * 24)

print("le nombre de minute depuis le début du mois est" , résulat , 'minutes')