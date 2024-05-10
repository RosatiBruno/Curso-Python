idade = int(input("Digite sua idade: "))

while (idade > 0) :
    sexo = input("Digite seu sexo (M ou F): ")
    if (sexo == "m") or (sexo == "M") :
        if (idade > 0) :
            print(f"Boa noite, Senhor. Sua idade é: {idade}")
        else :
            break
    elif (sexo == "f") or (sexo == "F") :
        if (idade > 0) :
         print(f"Boa noite, Senhora. Sua idade é: {idade}")
        else :
            break
    idade = int(input("\nDigite sua idade: "))
