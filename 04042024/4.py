nNumeros = int(input("Digite o valor de N números para serem somados: "))

contador = 1
soma = 0

while contador <= nNumeros:
    soma += contador
    contador += 1

print(f'Soma: {soma}')