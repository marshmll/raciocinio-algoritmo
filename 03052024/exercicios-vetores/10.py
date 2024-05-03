valores = [0, 0, 0, 0, 0]

valores[0] = float(input(f"Digite um número (1 de {len(valores)}): "))

maiorVal = valores[0]
menorVal = valores[0]

media = valores[0] / len(valores)

i = 1
while i < len(valores):
  valores[i] = float(input(f"Digite um número ({i + 1} de {len(valores)}): "))

  if valores[i] > maiorVal:
    maiorVal = valores[i]
  elif valores[i] < menorVal:
    menorVal = valores[i]
  
  media += valores[i] / len(valores)

  i += 1

print(f"Valores lidos: {valores}")
print(f"Maior valor lido: {maiorVal}")
print(f"Menor valor lido: {menorVal}")
print(f"Média dos valores lidos: {media}")