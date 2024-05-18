from random import randrange

letras = []
letrasEmbaralhadas = []

for i in range(0 + 97, 26 + 97):
  letras.append(chr(i))

for i in range(len(letras)):
  indiceAleatorio = randrange(len(letras))
  
  while letras[indiceAleatorio] in letrasEmbaralhadas:
    indiceAleatorio = randrange(len(letras))

  letrasEmbaralhadas.append(letras[indiceAleatorio])

print(letrasEmbaralhadas)