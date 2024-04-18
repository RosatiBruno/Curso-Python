nmr = int(input("Digite um número qualquer \n"))

if (nmr < -1 and nmr > -100) :
    print(f"O número {nmr} esta entre -100 e -1")
elif (nmr > 1 and nmr < 100) :
    print(f"O número {nmr} esta entre 100 e 1")
else :
    print(f"O número {nmr} não está entre -100 e -1 nem entre 1 e 100")