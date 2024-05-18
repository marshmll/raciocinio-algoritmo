text = input("Digite um texto: ")

words = []

string = ""
for char in text:

  if char != ' ':
    string = string + char
  else:
    words.append(string)
    string = ""

words.append(string)

print(words)