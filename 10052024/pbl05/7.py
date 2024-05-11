soma = 0

# Soma 50 números que são pares
for i in range(0, 101):
  if i % 2 == 0:
    soma += i
  
print(f"A soma dos 50 primeiros números pares é de {soma}")