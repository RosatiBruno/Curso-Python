totalCompra = float(input("Informe o valor total da compra: \n"))
parcelas = int(input("Informe o número de parcelas que deseja (1, 3, 5 ou 10): \n"))

while (parcelas != 1) and (parcelas != 3) and (parcelas != 5) and (parcelas != 10) :
    print(f"Número de parcelas indisponível! Digite novamente!")
    parcelas = int(input("Informe o número de parcelas que deseja (1, 3, 5 ou 10): \n"))

if (parcelas == 1) :
    desc = totalCompra * .05
    totalCompra -= desc

elif (parcelas == 3) :
    totalCompra = totalCompra

elif (parcelas == 5) :
    desc = totalCompra * .02
    totalCompra += desc

elif (parcelas == 10) :
    desc = totalCompra * .08
    totalCompra += desc

print(f"O novo valor da compra será de R${totalCompra}")
