vectorSize = 0

while vectorSize <= 0:
  vectorSize = int(input('Digite o tamanho das listas: '))

A = [0] * vectorSize
B = [0] * vectorSize
C = [0] * vectorSize

for i in range(len(A)):
  A[i] = int(input(f"Digite o elemento nº {i + 1} do vetor A: "))

print()

for i in range(len(B)):
  B[i] = int(input(f"Digite o elemento nº {i + 1} do vetor B: "))

for i in range(len(C)):
  C[i] = A[i] + B[i]

print(f"\nO vetor-soma dos vetores A e B é: {C}")

