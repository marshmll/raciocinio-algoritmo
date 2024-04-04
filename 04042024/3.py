soma = 0

contador = 0

entrada = float(input('Digite um número (-1 para encerrar): '))

while entrada != -1:
    soma += entrada
    entrada = float(input('Digite um número (-1 para encerrar): '))
    contador += 1


print(f'A média das notas inseridas é de {soma / contador}')