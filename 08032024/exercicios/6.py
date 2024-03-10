def main():
  valorPorQuiloEmReais = getFloat("Digite o valor (por kg) do produto: ")
  pesoDoProduto = getFloat("Digite o peso (em kg) do produto: ")

  valorTotalDoProduto = valorPorQuiloEmReais * pesoDoProduto

  print(f"\nO valor total do produto é de {valorTotalDoProduto:.2f} reais.\n")

def getFloat(prompt):
  while True:
    try:
      valor = float(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()