from random import randrange

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(nums)):
    nums[i] = randrange(0, 101)

userInput = int(input("Digite um número para verificar se existe na lista: "))

for i, num in enumerate(nums):
    if userInput == num:
        print(f"O número digitado foi {userInput} e existe na posição {i}")
        break
else:
    print(f"O número digitado foi {userInput} e não existe no vetor.")