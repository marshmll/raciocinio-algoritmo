# Vetor A com 6 números inteiros
A = [1, 0, 5, -2, -5, 7]

# Variável do tipo int que armazena a soma
soma = A[0] + A[1] + A[5]

print(f"Soma: {soma}")

# Muda o valor do index 4 para 100
A[4] = 100

# Itera e printa os valores
i = 0
while i < len(A):
    print(f"Valor de A[{i}] = {A[i]}")
    i += 1