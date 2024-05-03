strings = ["", "", "", "", "", "", "", "", "", ""]

i = 0
while i < len(strings):
  strings[i] = input(f"Digite a {i + 1}º palavra: ")
  i += 1

size = 0
while size < len(strings):
  size += 1

print(f"O tamanho do vetor é de {size}.")