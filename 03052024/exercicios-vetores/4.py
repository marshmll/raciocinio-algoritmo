numbers = [0, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(numbers):
  numbers[i] = float(input(f"Digite um número ({i + 1} de {len(numbers)}): "))
  i += 1

while True:
  X = int(input("Digite um valor para o índice X: "))
  if X < 0 or X > len(numbers) - 1:
    print("Por favor, digite um índice válido.")
  else:
    break

while True:
  Y = int(input("Digite um valor para o índice Y: "))
  if Y < 0 or Y > len(numbers) - 1:
    print("Por favor, digite um índice válido.")
  else:
    break

sum = numbers[X] + numbers[Y]

print(f"A soma dos números nas posições X ({X}) e Y ({Y}) é de: {sum} ({numbers[X]} + {numbers[Y]})")