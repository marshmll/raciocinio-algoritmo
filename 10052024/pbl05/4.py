qtdeIdades = -1

while qtdeIdades <= 0:
  qtdeIdades = int(input("Digite quantas idades você deseja: "))

idades = [0] * qtdeIdades

for i in range(len(idades)):
  idades[i] = int(input(f"Digite uma idade ({i + 1} de {len(idades)}): "))

media = 0

for idade in idades:
  media += idade / len(idades)

print(f'A média das idades digitadas é de {media}')
