total = 0
cont = 0
tabuada = int(input("Digite o número a ter a tabuada calculada: "))
numeroFinal = int(input("Digite até qual número a tabuada deve ser calculada: "))

for cont in range (1, numeroFinal + 1, 1) :
    total = tabuada * cont
    print(f"{tabuada} X {cont} = {total}")
