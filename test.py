from random import choice

"""
with open("C:/Users/eriol/Desktop/anagramme/liste5.txt") as file:
    lines = file.readlines()  
# on transforme en liste :
liste_5m = []
for line in map(str.rstrip, lines):
    liste_5m.append(line)
 
mot_a_trouver = choice(liste_5m)
print(mot_a_trouver)
"""

with open("C:/Users/eriol/Desktop/anagramme/liste.txt") as file:
    lines = file.readlines()  
# on transforme en liste :
liste_5m = []
for line in map(str.rstrip, lines):
    if len(line) == 3:
        liste_5m.append(line)

print(liste_5m)