notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
media = 0

i = 0
while i < len(notas):
  notas[i] = float(input(f"Digite uma nota ({i + 1} de {len(notas)}): "))

  media += notas[i] / len(notas)

  i += 1

print(f"A média geral das notas fornecidas é aproximadamente de {media}")