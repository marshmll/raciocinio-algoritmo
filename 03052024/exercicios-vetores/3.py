# Inicializa vetores
realNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
squaredNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(realNumbers):
  # Coleta número real do usuário
  realNumbers[i] = float(input(f"Digite um número real ({i + 1} de {len(realNumbers)}): "))

  # Armazena o valor² no vetor dos quadrados
  squaredNumbers[i] = realNumbers[i] ** 2

  i += 1

print(f"\nNúmeros: {realNumbers}")
print(f"Quadrados dos números: {squaredNumbers}")

