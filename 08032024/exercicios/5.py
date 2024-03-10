def main():
  idadeEmAnos = getInt("Digite a sua idade: ")
  mesesPorAno = 12

  idadeEmMeses = idadeEmAnos * mesesPorAno

  print(f"\nSua idade em meses é de aproximadamente {idadeEmMeses} meses.\n")

def getInt(prompt):
  while True:
    try:
      valor = int(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()