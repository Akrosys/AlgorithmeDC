from random import randint
import time

a, b = 0, 10
N = 2000
liste = [randint(a,b) for _ in range(N)]
tps1 = time.time()

#tri d'une liste
for i in range(len(liste)):
  cle = liste[i]
  j = i
  while j > 0 and liste[j-1] > cle:
    liste[j] = liste[j-1]
    j = j-1
  liste[j] = cle
tps2 = time.time()
print(tps2 - tps1)