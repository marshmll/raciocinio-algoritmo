text = input("Digite um texto qualquer: ")

vowels = ['a', 'e', 'i', 'o', 'u']

amountOfVowels = 0

for char in text:
  for vowel in vowels:
    if char.lower() == vowel:
      amountOfVowels += 1
      print(f"Encontrada uma vogal: {char}.")
      break
  
print(f"Foram encontradas {amountOfVowels} vogais")