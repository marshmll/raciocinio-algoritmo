vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

moda = 0
repeticoesDaModa = 0

for numeroAnterior in vetor:
  repeticoes = 0

  for numero in vetor:
    if numeroAnterior == numero:
      repeticoes += 1
  
  if repeticoes > repeticoesDaModa:
    repeticoesDaModa = repeticoes
    moda = numeroAnterior

print(f"{moda}")