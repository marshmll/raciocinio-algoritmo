def main():
  anoDeNascimento = getInt("Digite o ano do seu nascimento: ")
  anoAtual = 2024

  idade = anoAtual - anoDeNascimento

  print(f"\nSua idade é de {idade} anos (até o final de {anoAtual}).\n")

# Esta implementação assegura o gerenciamento de erros caso o usuário insira um valor inválido.
def getInt(prompt):
  while True:
    try:
      valor = int(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()