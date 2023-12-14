from collections import Counter

L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6, 2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

# Utiliser Counter pour compter les occurrences de chaque élément
counter = Counter(L1)

# Trouver l'élément le plus fréquent et son nombre d'occurrences
nombre_plus_frequent, occurrences = counter.most_common(1)[0]

print(f"Le nombre le plus fréquent dans la liste est {nombre_plus_frequent}, il apparaît {occurrences} fois.")
