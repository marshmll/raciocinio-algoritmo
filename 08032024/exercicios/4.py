def main():
  notas = []

  for i in range(1, 5):
    nota = getFloat(f"Digite a nota ({i} de 4): ")
    notas.append(nota)

  media = 0

  for nota in notas:
    media += nota / len(notas)

  print(f"\nA média das 4 notas é de {media} pontos.\n")

def getFloat(prompt):
  while True:
    try:
      valor = float(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()