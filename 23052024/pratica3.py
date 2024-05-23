matrix = []
counter = 1

for i in range(3):
    matrix.append([])

    for j in range(3):
        matrix[i].append(counter)
        counter += 1

print(matrix)

for row in matrix:
    print(row)

for row in matrix:
    for col in row:
        print(col)

matrix[0][0] = 20
matrix[1][2] = 15
matrix[2][1] = 19

print(matrix)

for row in matrix:
    print(row)

for row in matrix:
    for col in row:
        print(col)

soma = matrix[0][0] + matrix[1][0]
subtracao = matrix[2][2] - matrix[2][1]
multiplicacao = matrix[0][1] * matrix[2][0]
divisao = matrix[1][2] / matrix[0][2]

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')