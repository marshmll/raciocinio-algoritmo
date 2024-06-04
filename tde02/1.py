matrixSize = 5

matrix = [
    [0] * matrixSize,
    [0] * matrixSize,
    [0] * matrixSize,
    [0] * matrixSize,
    [0] * matrixSize
]

for i in range(matrixSize):
    matrix[i][i] = 1

for row in matrix:
    print(row)