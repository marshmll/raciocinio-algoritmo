from random import randrange

acertos = 0

numerosSorteados = [0, 0, 0, 0, 0, 0]

i = 0
while i < len(numerosSorteados):
    numerosSorteados[i] = randrange(0, 256)
    i += 1

numerosJogados = [0, 0, 0, 0, 0, 0]

i = 0
while i < len(numerosSorteados):
    numerosJogados[i] = int(input(f"Digite um número ({i + 1} de 6): "))
    i += 1

i = 0
while i < len(numerosJogados):

    j = 0
    while j < len(numerosSorteados):
        if numerosJogados[i] == numerosSorteados[j]:
            acertos += 1
            break
        j += 1
    
    i += 1

print(f"Suas jogadas: {numerosJogados}")
print(f"Números sorteados: {numerosSorteados}")
print(f"VOCÊ ACERTOU {acertos} NÚMERO(S)")