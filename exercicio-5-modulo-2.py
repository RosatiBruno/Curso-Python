slr = float(input("Informe seu salário \n"))
tmpEmp = int(input("Informe quantos anos você tem de empresa \n"))

if (tmpEmp > 10) :
    bns = slr * .3

elif (tmpEmp > 5 and tmpEmp <= 10) :
    bns = slr * .2

else :
    bns = slr * .1

slr += bns
print(f"Seu bônus será de: {bns}, seu novo salário será de: {slr}")
