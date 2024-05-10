todasNotas = list()
nota = float(input("Digite uma nota (-1 para encerrar): "))

while (nota >= 0) :
    try :
        todasNotas.append(nota)
        nota = float(input("Digite uma nota (-1 para encerrar): "))

    except ValueError:
        print("Digite apenas números!")

if todasNotas :  # ! Verifica se a lista está vazio, caso esteja vai pro else
    media = sum(todasNotas) / len(todasNotas)
    print(f"A média das notas digitadas é: {media}")

else :
    print("Nenhuma nota foi digitada.")
