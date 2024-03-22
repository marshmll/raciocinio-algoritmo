pdl = int(input("Digite seu PdL: "))

if pdl <= 999:
    print("Seu elo é: FERRO")
elif pdl < 2000:
    print("Seu elo é: BRONZE")
elif pdl < 3000:
    print("Seu elo é: PRATA")
elif pdl < 4000:
    print("Seu elo é: OURO")
elif pdl < 5000:
    print("Seu elo é: PLATINA")
elif pdl < 6000:
    print("Seu elo é: DIAMANTE")
elif pdl < 7000:
    print("Seu elo é: MESTRE")
elif pdl < 8000:
    print("Seu elo é: GRÃO-MESTRE")
else:
    print("Seu elo é: DESAFIANTE")
