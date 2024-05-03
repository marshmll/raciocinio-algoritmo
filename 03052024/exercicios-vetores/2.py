# Inicializa vetor vazio com 6 espaços alocados
valores = [0, 0, 0, 0, 0, 0]

# Pede 6 números e coloca no vetor na posição 'i'
i = 0
while i < len(valores):
  valores[i] = int(input(f"Digite um número ({i + 1} de {len(valores)}): "))
  i += 1

# Mostra os valores
i = 0
while i < len(valores):
  print(valores[i])
  i += 1
