numeros = []

for i in range(0, 5):
    numeros.append(int(input(f'Digite um número inteiro ({i + 1} de 5): ')))

numerosOrdenados = sorted(numeros)

numerosOrdenadosInvertidos = list(reversed(numerosOrdenados))

print(f'Números: {numeros}')
print(f'Números ordenados: {numerosOrdenados}')
print(f'Números ordenados e invertidos: {numerosOrdenadosInvertidos}')

print(f'Tamanho da lista: {len(numeros)}')

print(f'Menor número: {min(numeros)}')
print(f'Maior número: {max(numeros)}')

print(f'Soma de todos os valores: {sum(numeros)}')