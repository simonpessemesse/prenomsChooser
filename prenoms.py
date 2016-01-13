#!/usr/bin/env python
# -*- coding: utf-8 -*-

nom=input(" quel Nom Veux Tu Donner Au Resultat?   ")

liste=[]
import fileinput
for line in fileinput.input("prenomsLave"):
    prenom=""
    i=0
    while(not line[i].isspace()):
        prenom+=line[i]
        i=i+1
    liste.append(prenom)

print(liste)
import random
random.shuffle(liste)
print(liste)
prenoms=liste




prenom=["Ael",
"Adriel",
"Damián / Demian ",
"Elio ",
"Evo",
"Gael",
"Julien/Julian",
"Leo",
"Leonel / Lionel",
"Lihue / Lihuel ",
"Lisandro / Elisandro ",
"Lucas ",
"Mael",
"Mateo / Matías / Mathías ",
"Nicolás ",
"Noé ",
"Sebastián ",
"Tahiel",
"Teo",
"Tiago",
"Ulises"
]


from functools import cmp_to_key
def cilo(a,b):
    print(a," (1) ou (2)",b)

    i=input()
    if str(i)=="1":
        return -1
    else:
        return 1

prenoms.sort(key=cmp_to_key(cilo))
listeFinale=prenoms
i=1
for l in listeFinale:

    print(l)
    i+=1
with open(nom, 'w') as f:
    for n in listeFinale:
        print(n,file=f)
