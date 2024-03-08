weight = float(input("Digite seu peso: "))
height = float(input("Digite sua altura: "))

imc = weight / (height ** 2);

print(f"\nSeu IMC (Índice de Massa Corporal) é: {imc:.2f}\n")