#!/bin/python3.6

dataUtilisateur = input("Les chiffres séparés des virgules : ")
listeData = dataUtilisateur.split(",")
tupleData = tuple(listeData)

print(listeData)
print(tupleData)