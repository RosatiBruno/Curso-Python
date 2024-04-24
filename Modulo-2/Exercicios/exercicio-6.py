print("*******************")
print("*   1 - Maçã      *")
print("*   2 - Banana    *")
print("*   3 - Laranja   *")
print("*******************")

fruta = int(input("Digite o número correspondente a fruta escolhida: \n"))

while (fruta != 1) and (fruta != 2) and (fruta != 3) :
    print(f"A opção {fruta} não é válida!")
    fruta = int(input("Digite o número correspondente a fruta escolhida: \n"))

if (fruta == 1 ) :
    prc = 2.30
    qlFruta = "Maçã"

elif (fruta == 2) :
    prc = 1.85
    qlFruta = "Banana"

elif (fruta == 3) :
    prc = 3.60
    qlFruta = "Laranja"

qtd = int(input(f"Informe quantas unidades de {qlFruta} deseja comprar: \n"))
prcFinal = prc * qtd

print(f"O preço final ficará em: R${prcFinal: .2f}")