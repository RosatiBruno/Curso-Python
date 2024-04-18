salar = float(input("Digite seu salário \n"))
tempEmpr = int(input("Digite a quantos anos você trabalha na empresa \n"))

bns10 = salar * 0.10
bns20 = salar * 0.20

if (tempEmpr > 5) :
    salarFinal = salar + bns20
    print(f"Você receberá {bns20} de bônus, totalizando {salarFinal}")
else :
    salarFinal = salar + bns10
    print(f"Você receberá {bns10} de bônus, totalizando {salarFinal}")
    