numerosPares = 0
numerosImpares = 0

contador = 0
while contador < 10:
    entrada = int(input(f'Digite um número ({contador + 1} de 10): '))

    if entrada % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1
    
    contador += 1

print(f'Números Pares: {numerosPares}\n Números Impares: {numerosImpares}')