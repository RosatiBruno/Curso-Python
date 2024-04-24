frase = input("Digite uma frase: ")
qtdLetras = len(frase)
while (qtdLetras < 10) or (qtdLetras > 30) :
    print("Tamanho de frase inválido!\n")
    frase = input("Digite uma frase: ")
    qtdLetras = len(frase)

print(f"Frase com os espaços: \n{frase}")
print(f"Frase sem os espaços: \n", end="")
for cont in range (0, qtdLetras, 1) : 
    if (frase[cont] != " ") :
        print(frase[cont], end="")
