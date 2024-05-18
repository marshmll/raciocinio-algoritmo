text = input("Digite um texto: ")

words = text.split(' ')
lengths = []

for word in words:
  lengths.append(len(word))

biggestLength = max(lengths)
smallestLength = min(lengths)

biggestWord = words[lengths.index(biggestLength)]
smallestWord = words[lengths.index(smallestLength)]

print(f'Maior: {biggestWord}')
print(f'Menor: {smallestWord}')