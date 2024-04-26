
# ! Função Lambda que soma 5 ao nmr1 e dps multiplica pelo nmr2
somaMultiplicacao = lambda nmr1, nmr2 : (nmr1 + 5) * nmr2

# ! Digitação dos Valores de nmr1 e nmr2
nmr1 = int(input("Digite o primeiro número: "))
nmr2 = int(input("Digite o segundo número: "))

# ! Chama a Função Lambda dentro do print
print(somaMultiplicacao(nmr1, nmr2))
