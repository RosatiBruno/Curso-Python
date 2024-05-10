def validarString(palavra, min, max) :
    stringDigitada = input(palavra)
    respLen = len(stringDigitada)
    while (min > respLen) or (respLen > max) :
        stringDigitada = (input("Digite uma frase: "))
        respLen = len(stringDigitada)
    return stringDigitada

resposta = validarString("Digite uma frase: ", 5, 20)
print(f"Resposta: {resposta}")
