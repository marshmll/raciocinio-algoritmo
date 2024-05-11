numeros = [0] * 10

for i in range(0, 10):
  numeros[i] = int(input(f"Digite um número({i + 1} de 10): "))

## Continua enquanto a lista não estiver ordenada
sorted = False
while not sorted:
  hasSwapped = False

  # Itera em pares pelo vetor
  for i in range(len(numeros) - 1):
    # Se o número da esquerda for maior que o da direita, inverte
    if numeros[i] > numeros[i + 1]:
      temp = numeros[i]
      numeros[i] = numeros[i + 1]
      numeros[i + 1] = temp
      hasSwapped = True
  
  # Verifica se foi feita alguma inversão
  # Se não, significa que está ordenado.
  if not hasSwapped:
    sorted = True

print(f'A lista de números ordenada é {numeros}')

