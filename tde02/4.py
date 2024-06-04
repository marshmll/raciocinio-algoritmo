def soma_elementos(lista):
    soma = 0
    
    for elemento in lista:
        soma += elemento

    return soma


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = soma_elementos(lista)

print(soma)
