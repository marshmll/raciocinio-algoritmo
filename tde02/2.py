matrix = [
    [0] * 4,
    [0] * 4,
    [0] * 4,
    [0] * 4,
]

for i in range(4):
    for j in range(4):
        matrix[i][j] = int(input(f"Digite um número (posição {i}, {j}): "))

biggestNumbersPerRow = []

for row in matrix:
    biggestNumbersPerRow.append(max(row))

biggestNumber = max(biggestNumbersPerRow)
biggestNumberIndexes = []

for i, row in enumerate(matrix):
    found = False
    for j, number in enumerate(row):
        if number == biggestNumber:
            biggestNumberIndexes = [i, j]
            found = True
            break
    if found:
        break


print(f"O maior número digitado foi {biggestNumber} e está nos índices {biggestNumberIndexes}")
