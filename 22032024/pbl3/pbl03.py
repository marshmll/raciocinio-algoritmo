print("Vc está em uma floresta e precisa escolher um caminho para seguir.\n")
print("A sua esquerda, vc observa um rio de correnteza forte, cheio de pedras.")
print("A sua direita, vc observa uma montanha alta, pedrosa, com neve no seu topo.\n")

print("Qual caminho vc escolherá?")

while(True):
    direcao = input("Resposta: ").lower()
    if direcao == "esquerda" or direcao == "direita":
        break
    else:
        print("Opcao invalida, tente novamente.")


if direcao == "esquerda":
    print("Vc escolheu o rio.")
    print("A correnteza parece muito forte, entretanto vc precisa chegar ao outro lado.")

    while(True):
        resposta = input("Vc deseja tentar atravessar o rio? (s/n): ")
        if resposta == "s" or resposta == "n":
            break
        else:
            print("Opcao invalida, tente novamente.")

    if resposta == "s":
        print("Vc entra no rio. A correnteza te puxa para baixo e vc não consegue escapar. Alguns segundos depois, vc morre afogado. FIM")
    elif resposta == "n":
        print("Vc decide não entrar no rio, e vai embora para a sua casa. FIM")
elif direcao == "direita":
    print("Vc escolheu a montanha.")

    while(True):
        resposta = input("Vc deseja subir na montanha? (s/n): ")
        if resposta == "s" or resposta == "n":
            break
        else:
            print("Opcao invalida, tente novamente.")

    if resposta == "s":
        print("Vc sobe a montanha, e no meio do caminho se sente cansado. Vc deita para descansar.")
        print("Enquanto vc dorme, um urso pardo te encontra. Vc virou almoco de urso pardo. FIM")
    elif resposta == "n":
        print("Vc desiste de tentar escalar a montanha e vai para casa. FIM")