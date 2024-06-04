def contar_caracteres(string, caracter):
    repeticoes = 0    
    
    for char in string:
        if char == caracter:
            repeticoes += 1

    return repeticoes

string = "Professora Marina"

repeticoes = contar_caracteres(string, 'o')

print(repeticoes)
