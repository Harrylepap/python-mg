#!/bin/python3.6

def factoriel(nombreDonnee):
          if  nombreDonnee == 0 :
                    return 1
          return nombreDonnee * factoriel(nombreDonnee - 1)

dataUtilisateur = int(input("Entrez un nombre = "))
print(factoriel(dataUtilisateur))