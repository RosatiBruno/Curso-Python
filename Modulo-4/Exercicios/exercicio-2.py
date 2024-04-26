def contagem(final, inicial = 0, passo = 1) :
    for cont in range (inicial, final+1, passo) :
        print(f"{cont}", end = " ")

inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
passo = int(input("Digite o passo: "))

contagem(final, inicial, passo)
