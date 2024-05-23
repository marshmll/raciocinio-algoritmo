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