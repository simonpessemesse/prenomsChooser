#!/usr/bin/env python
# -*- coding: utf-8 -*-

prenoms=["Ael",
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
for l in listeFinale:
    print(l)
