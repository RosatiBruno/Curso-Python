def verificar(nmrDigitado, lista) :
    cont = 0
    while cont < len(lista) :

        if (lista[cont] == nmrDigitado) :
            return nmrDigitado, cont
        
        cont += 1
    return -1

lista = (1, 3, 5, 7, 9, 11)                 # ! Lista com os valores de teste
while True :
    try :
        nmrDigitado = int(input("Digite um número inteiro: "))
        break

    except ValueError :
        print("Valor inválido!")

respostaContem = verificar (nmrDigitado, lista)

if (respostaContem != -1) :
    numero, posicao = respostaContem
    print(f"O número {numero} está presente na Lista na posição {posicao + 1}")

else :
    print(f"O número não consta na lista!")
