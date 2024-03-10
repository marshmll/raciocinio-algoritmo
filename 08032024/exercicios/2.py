def main():
  valorAluguelCarroPorDia = 100.00
  diasCarroAlugado = getFloat("Digite por quantos dias o carro foi alugado: ")
  valorTotalAluguel = valorAluguelCarroPorDia * diasCarroAlugado

  print(f"\nO valor total do aluguel do carro será de {valorTotalAluguel:.2f} reais.\n")

def getFloat(prompt):
  while True:
    try:
      valor = float(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()