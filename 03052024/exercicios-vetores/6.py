numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

numeros[0] = int(input(f"Digite um número (1 de {len(numeros)}): "))

maiorNum = numeros[0]
menorNum = numeros[0]

i = 1
while i < len(numeros):
  numeros[i] = int(input(f"Digite um número ({i + 1} de {len(numeros)}): "))

  if numeros[i] > maiorNum:
    maiorNum = numeros[i]
  
  elif numeros[i] < menorNum:
    menorNum = numeros[i]

  i += 1


print(f"Maior número do vetor: {maiorNum}")
print(f"Menor número do vetor: {menorNum}")