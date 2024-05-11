numero = 0

while numero not in range(1, 11):
  numero = int(input('Digite um número entre 1 e 10: '))

for i in range(1, 11):
  print(f'{numero} * {i} = {numero * i}')

