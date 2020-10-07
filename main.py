#Minimum Liste
print("Minimum Liste :")

L = [7,8,6,4,42,5,18,6]
min = L[0]

for i in range(len(L)):
    if min > L[i]:
        min = L[i]
print(min)

#Simple echange
print("Echange de valeur")
A = 8
B = 10
C = 0

C = A
A = B
B = C

print("A =", A, "B =", B)

#Afficher le carré d'un nombre donné
print("Entrer la valeur de x")
x = int(input())
res = x*x
print("x au carré = ", res)

#Positif ou negatif ?
print("Indiquez un nombre pour savoir s'il est négatif ou positif ?")
nbre = int(input())
if nbre > 0:
  print("positif")
else:
  print("negatif")

#Positif ou négatif avec deux nombre
print("Produit négatif ou positif ?")
nbreA = int(input())
nbreB = int(input())

if (nbreA > 0 and nbreB > 0) or (nbreA < 0 and nbreB < 0) or (nbreA == 0 or nbreB == 0):
  print("le produit est positif")
else:
  print("Le produit est négatif")

#Afficher les 10 nombres suivants le nombre indiqué
print("Entrez un nombre de départ :")
nbreDepart = int(input())
i = 10
while i != 0:
  nbreDepart += 1
  i -= 1
  print(nbreDepart)

#A partir d'un nombre positif, donner la somme de tous les entiers jusqu'à ce nombre
print("Indiquer un nombre pour la somme des entiers jusquà ce nombre :")
nombreAdditions = int(input())
res = 0
while nombreAdditions > 0:
  res = res + nombreAdditions
  nombreAdditions -= 1
print("resultat :", res)