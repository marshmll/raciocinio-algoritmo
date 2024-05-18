import os

tableState = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

amountOfRounds = 0

hasWiner = False
winner = ''

player = ''

while not (player == 'X') and not (player == 'O'):
  player = input('Digite o jogador que irá começar (x ou o): ').upper()

while not hasWiner:
  
  os.system('cls' if os.name == 'nt' else 'clear')

  # Se o tabuleiro está cheio
  if (amountOfRounds == 9):
    print("Velha! Ninguém venceu.")
    
    for i in range(3):
      for j in range(3):
        print(tableState[i][j], end=" ")
      print()
    print()
    break

  # Printa o tabuleiro
  for i in range(3):
    for j in range(3):
      print(tableState[i][j], end=" ")
    print()
  print()
  
  validPosition = False
  nextPosIndexes = []
  
  # Enquanto o jogador não informar uma posição válida
  while not validPosition:
    nextPos = int(input(f'Digite a posição do {player}: '))

    validPosition = True

    for i, row in enumerate(tableState):
      if nextPos in row:
        nextPosIndexes = [i, row.index(nextPos)]
        validPosition = True
        break
    else:
      validPosition = False
  
  # Coloca o jogador no tabuleiro na posição correta
  tableState[nextPosIndexes[0]][nextPosIndexes[1]] = player
  amountOfRounds += 1

  # Verifica ombinações horizontais
  for row in tableState:
    if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
      hasWiner = True
      winner = 'X'
      break

    elif row[0] == 'O' and row[1] == 'O' and row[2] == 'O':
      hasWiner = True
      winner = 'O'
      break
  
  # Verifica combinações verticais
  for i in range(0, 3):
    if tableState[0][i] == 'X' and tableState[1][i] == 'X' and tableState[2][i] == 'X':
      hasWiner = True
      winner = 'X'
      break
    elif tableState[0][i] == 'O' and tableState[1][i] == 'O' and tableState[2][i] == 'O':
      hasWiner = True
      winner = 'O'
      break
  
  # Verifica combinações diagonais
  if tableState[0][0] == 'X' and tableState[1][1] == 'X' and tableState[2][2] == 'X':
    hasWiner = True
    winner = 'X'
    break
  elif tableState[0][2] == 'X' and tableState[1][1] == 'X' and tableState[2][0] == 'X':
    hasWiner = True
    winner = 'X'
    break
  elif tableState[0][0] == 'O' and tableState[1][1] == 'O' and tableState[2][2] == 'O':
    hasWiner = True
    winner = 'O'
    break
  elif tableState[0][2] == 'O' and tableState[1][1] == 'O' and tableState[2][0] == 'O':
    hasWiner = True
    winner = 'O'
    break

  if player == 'X':
    player = 'O'
  else:
    player = 'X'

# Se o jogo encerrou com um vencedor
if hasWiner:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print(f'O vencedor é o {winner}!!\n')
  
  for i in range(3):
    for j in range(3):
      print(tableState[i][j], end=" ")
    print()
  print()