matrix = []

rows = 5
cols = 4

bigestGrade = 0

for i in range(rows):
    matrix.append([])
    
    print(f"Aluno nº {i + 1}")

    registrationNumber = int(input("Digite o número da matrícula: "))
    examsGradeMean = float(input("Digite a média das provas: "))
    essaysGradeMean = float(input("Digite a média dos trabalhos: "))
    finalGrade = examsGradeMean + essaysGradeMean

    matrix[i].append(registrationNumber)
    matrix[i].append(examsGradeMean)
    matrix[i].append(essaysGradeMean)
    matrix[i].append(finalGrade)

    if i == 0:
        biggestGrade = matrix[i][3]
    elif matrix[i][3] > biggestGrade:
        biggestGrade = matrix[i][3]

for row in matrix:
    if biggestGrade in row:
        print(f"A matrícula do aluno com a maior nota final é: {row[0]}")

