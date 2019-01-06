#!/bin/python3.6

dataUtilisateur = input()
dimensions = [int(x) for x in dataUtilisateur.split(",")]
lignes = dimensions[0]
colonnes = dimensions[1]

listes = [[0 for colonne in range(colonnes)] for ligne in range(lignes) ]
for ligne in range(lignes):
          for colonne in range(colonnes):
                    listes[ligne][colonne] = ligne*colonne

print(listes)