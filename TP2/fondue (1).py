BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Nmbre de convives :\n"))

fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

print (f"Pour faire une fondue fribourgeoise pour {nbConvives}, il vous faut : \n- {fromage} gr de fromage\n- {eau} dl d`eau\n- {ail} gousse(s) d'ail\n- {pain} gr de pain")


