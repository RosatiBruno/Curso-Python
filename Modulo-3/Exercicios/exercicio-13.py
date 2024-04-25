soma = 0
media = 0
qtdNumero = 0

while True :
    numero = int(input("Digite um numero positivo: "))
    if (numero > 0) :
        soma += numero
        qtdNumero += 1
    else :
        break
media = soma / qtdNumero
print(f"A média dos valores é: {media}")
