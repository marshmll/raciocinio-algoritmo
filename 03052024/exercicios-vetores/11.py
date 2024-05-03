valores = [0, 0, 0, 0, 0]

valores[0] = float(input(f"Digite um número (1 de {len(valores)}): "))

maiorVal = valores[0]
menorVal = valores[0]

posMaiorVal = 0
posMenorVal = 0

i = 1
while i < len(valores):
  valores[i] = float(input(f"Digite um número ({i + 1} de {len(valores)}): "))

  if valores[i] > maiorVal:
    maiorVal = valores[i]
    posMaiorVal = i

  elif valores[i] < menorVal:
    menorVal = valores[i]
    posMenorVal = i

  i += 1

print(f"Posição do maior valor: índice [{posMaiorVal}]")
print(f"Posição do menor valor: índice [{posMenorVal}]")