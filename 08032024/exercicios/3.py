def main():
  temperaturaEmCelsius = getFloat("Digite a temperatura em Celsius: ")
  temperaturaEmFahrenheit = celsiusParaFahrenheit(temperaturaEmCelsius)

  print(f"\nA temperatura digitada, em graus farenheit, é de {temperaturaEmFahrenheit}°F\n")

def celsiusParaFahrenheit(temp):
  return (temp * 9/5) + 32

def getFloat(prompt):
  while True:
    try:
      valor = float(input(prompt))
      break
    except ValueError:
      pass
  return valor

main()