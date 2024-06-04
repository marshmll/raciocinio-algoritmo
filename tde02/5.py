def e_palindromo(palavra):
    palavraInvertida = palavra[::-1]

    if palavra.lower() == palavraInvertida.lower():
        return True
    else:
        return False

palavra = "anana"

ePalindromo = e_palindromo(palavra)

if ePalindromo:
    print(f"A palavra {palavra} é palíndromo")
else:
    print(f"A palavra {palavra} não é palíndromo")
    
