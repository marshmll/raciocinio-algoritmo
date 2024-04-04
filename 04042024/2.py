nota = 0

while nota < 7:
    nota = float(input("Digite a sua nota: "))
    if nota < 7:
        print ("Nota inválida, tente novamente.")
print("Nota válida.")