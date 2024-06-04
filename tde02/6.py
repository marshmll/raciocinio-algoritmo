def maior_elemento(lista):
    maiorElemento = 0

    for i, elemento in enumerate(lista):
        if i == 0:
            maiorElemento = elemento
        elif elemento > maiorElemento:
            maiorElemento = elemento
    
    return maiorElemento

lista = [1, 12, 5, 3, 67, 1, 255]

maior = maior_elemento(lista)

print(maior)
