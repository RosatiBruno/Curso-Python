#
# ? Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final. Para este intervalo especificado pelo usuário, calcule e mostre na tela:
# * A quantidade de números inteiros e positivos;
# * A quantidade de números pares;
# * A quantidade de números impares;
# * A respectiva média de cada um dos itens anteriores;
# ? Será necessário criar uma variável distinta para cada somatório, para cada quantidade e para cada média solicitada.

valorInicial = int(input("Digite o valor inicial: "))
valorFinal = int(input("Digite o valor final: "))
totalInteiros = 0
totalPares = 0
totalImpares = 0
valorInt = 0
valorImp = 0
valorPar = 0
mediaInteiros = 0
mediaPares = 0
mediaImpares = 0
while (valorInicial <= valorFinal) :
    
    if (valorInicial % 2 == 0) :
        totalInteiros += 1
        valorPar += valorInicial
        valorInt += valorInicial
        totalPares += 1
        valorInicial += 1
    else :
        totalInteiros += 1
        totalImpares += 1
        valorImp += valorInicial
        valorInt += valorInicial
        valorInicial += 1

mediaInteiros = valorInt / totalInteiros
mediaImpares = valorImp / totalImpares
mediaPares = valorPar / totalPares
print(f"Int: {totalInteiros} Impar: {totalImpares} Par: {totalPares} media int: {mediaInteiros} media impar: {mediaImpares} media par: {mediaPares}")
    