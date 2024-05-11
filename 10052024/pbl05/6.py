numbersInRange = 0
numbersOutRange = 0

for i in range(0, 10):
  num = int(input(f'Digite um número ({i + 1} de 10): '))
  
  if num >= 10 and num <= 20:
    numbersInRange += 1
  else:
    numbersOutRange += 1

print(f'Você digitou {numbersInRange} números em um intervalo entre 10 e 20, e {numbersOutRange} números fora desse intervalo')