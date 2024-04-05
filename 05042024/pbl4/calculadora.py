operacao = -1 # VALOR ARBITRÁRIO APENAS PARA INICIALIZAÇÃO

while operacao != 0:
    print("Selecione uma operação aritmética: ")
    print("0. SAIR")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        operacao = int(input("Resposta: "))
        if operacao >= 0 and operacao <= 4:
            break
        else:
            print("Opção inválida, tente novamente.")

    if operacao != 0:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if operacao == 1:
            print(f"\nO RESULTADO DA OPERAÇÃO É IGUAL A {x + y}\n")
        elif operacao == 2:
            print(f"\nO RESULTADO DA OPERAÇÃO É IGUAL A {x - y}\n")
        elif operacao == 3:
            print(f"\nO RESULTADO DA OPERAÇÃO É IGUAL A {x * y}\n")
        elif operacao == 4:
            if y == 0:
                print(f"\nO RESULTADO DESTA OPERAÇÃO É UMA INDETERMINAÇÃO MATEMÁTICA.\n")
            else:
                print(f"\nO RESULTADO DA OPERAÇÃO É IGUAL A {x / y}\n")

