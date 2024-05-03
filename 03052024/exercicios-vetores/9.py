numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

qtdePositivos = 0
qtdeNegativos = 0

i = 0
while i < len(numeros):
  numeros[i] = float(input(f"Digite um número ({i + 1} de {len(numeros)}): "))
  i += 1

i = 0
while i < len(numeros):
  if numeros[i] < 0:
    qtdeNegativos += 1
  elif numeros[i] > 0:
    qtdePositivos += 1
  
  i += 1
  
print(f"A quantidade de números positivos é de {qtdePositivos}")
print(f"A quantidade de números negativos é de {qtdeNegativos}")