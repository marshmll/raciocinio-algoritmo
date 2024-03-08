def main():
	nome = input("Digite seu nome: ")
	cpf = getInt("Digite seu CPF (apenas números): ")
	telefone = getInt("Digite seu telefone (apenas números): ")
	anoDeNascimento = getInt("Digite seu ano de nascimento: ")    

	print()
	print(f"Nome: {nome}")
	print(f"CPF: {str(cpf)}")
	print(f"Telefone: {str(telefone)}")
	print(f"Ano de nascimento: {str(anoDeNascimento)}")
	print()

def getInt(prompt):
	while True:
		try:
			value = int(input(prompt))
			break
		except ValueError:
			pass
	return value
    
main()
  