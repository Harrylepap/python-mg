dataUtilisateur = int(input("Entrez le nombre magique : "))
resultats = dict()

for i in range(1, dataUtilisateur + 1):
          resultats[i] = i*i

print(resultats)