qtdePares = 0
qtdeImpares = 0

for i in range(0, 10):
  num = int(input(f'Digite um número ({i + 1} de 10): '))

  if num % 2 == 0:
    qtdePares += 1
  else:
    qtdeImpares += 1

print(f"A quantidade de números pares é de {qtdePares}, e a de ímpares é de {qtdeImpares}.")