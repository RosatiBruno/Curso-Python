nmr1 = float(input("Digite o primeiro valor: "))
nmr2 = float(input("Digite o segundo valor: "))
cont = 1
mlt = 0

while (cont <= nmr1) :
    mlt += nmr2
    cont += 1
print(f"{nmr1} X {nmr2} = {mlt: .2f}")