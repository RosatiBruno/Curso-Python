listaComDados = []  #! Declaração da lista vazia
imcLambda = lambda peso, altura: peso / (altura ** 2) #! Lambda para calcular o IMC
totalDeCadastros = 0
maiorIMC = 0
menorIMC = 100
while True :
    try :
        nome = input("Digite o nome: ")
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        listaComDados.append(nome)
        listaComDados.append(altura)
        listaComDados.append(peso)
        totalDeCadastros += 1

        while True :
            try : 
                rodarNovamente = int(input("Deseja cadastrar mais dados? 1 - Sim | 2 - Não: "))

                if (rodarNovamente == 1) :
                    break
                elif (rodarNovamente == 2) :
                    break
                elif (rodarNovamente != 1) :
                    print("Opção Inválidaaa!")

            except ValueError :
                print("Opção Inválida!")
        if (rodarNovamente == 2) :
            break

    except ValueError :
        print("Dado de tipo inválido!")

for cont in range (0, len(listaComDados), 3) :  #! Percorre a lista e calcula os IMCs
    nome = listaComDados[cont]
    altura = listaComDados[cont + 1]
    peso = listaComDados[cont + 2]
    imcCalculado = imcLambda(peso, altura)

    if imcCalculado > maiorIMC :
        maiorIMC = imcCalculado
        nomeMaiorIMC = nome
    
    if imcCalculado < menorIMC :
        menorIMC = imcCalculado
        nomeMenorIMC = nome

print(f"Total de cadastros: {totalDeCadastros}")
print(f"O maior IMC {maiorIMC:.2f} pertence a/o {nomeMaiorIMC}")#! Limita a 2 casas decimais
print(f"O menor IMC {menorIMC:.2f} pertence a/o {nomeMenorIMC}")#! Limita a 2 casas decimais
