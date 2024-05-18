from random import randint

tamanhoLista = randint(10, 20)
numeros = []

for i in range(tamanhoLista):
  numeros.append(randint(0, 256))

print(numeros)