numeroBase = int(input('Digite o número que você deseja a tabuada: '))

contador = 1

while contador <= 10:
    resultado = contador * numeroBase
    print(f'{contador} * {numeroBase} = {resultado}')
    contador += 1