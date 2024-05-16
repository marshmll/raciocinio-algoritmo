from random import randrange

numerosJogador1 = []
numersJogador2 = []

for i in range(2):
    numerosJogador1.append(randrange(1, 7))
    numersJogador2.append(randrange(1, 7))

somaJogador1 = sum(numerosJogador1)
somaJogador2 = sum(numersJogador2)

if somaJogador1 > somaJogador2:
    print(f'O jogador 1 venceu!')
elif somaJogador2 > somaJogador1:
    print(f'O jogador 2 venceu!')
else:
    print(f'Empate!')