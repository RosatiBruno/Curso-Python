nt1 = float(input("Informe sua nota na matéria 1 \n"))
nt2 = float(input("Informe sua nota na matéria 2 \n"))
nt3 = float(input("Informe sua nota na matéria 3 \n"))

md = (nt1 + nt2 + nt3) / 3

if (md >= 7) :
    print(f"Você foi aprovado, sua média foi: {md: .2f}")
else :
    print(f"Você não foi aprovado, sua média foi: {md: .2f}")
