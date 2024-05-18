pares = []
impares = []

for i in range(1, 11):
  if i % 2 == 0:
    pares.append(i)
  else:
    impares.append(i)

juncao = pares + impares;

print(juncao)