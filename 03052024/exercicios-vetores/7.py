numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

numeros[0] = int(input(f"Digite um número (1 de {len(numeros)}): "))

maiorNum = numeros[0]
indice = 0

i = 0
while i < len(numeros):
  numeros[i] = int(input(f"Digite um número ({i + 1} de {len(numeros)}): "))

  if numeros[i] > maiorNum:
    maiorNum = numeros[i]
    indice = i

  i += 1


print(f"Maior número do vetor é {maiorNum} e seu índice no vetor é {indice}")