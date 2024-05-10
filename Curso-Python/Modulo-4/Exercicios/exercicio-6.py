
# ! Função Validar os Inteiro
def validarInteiro(nmr1, nmr2) :
    if (nmr1 > 0) and (nmr2 > 0) :
        return nmr1, nmr2
    elif (nmr1 < 0) :
        while (nmr1 < 0) :
            nmr1 = int(input("Digite o 1° número novamente!: "))
    elif (nmr2 < 0) :
        while (nmr2 < 0) :
            nmr2 = int(input("Digite o 2° número novamente!: "))
    return nmr1, nmr2

# ! Função Somar os Números Entre nmr1 e nmr2
def somarNumeros(nmr1, nmr2) :
    soma = 0
    for cont in range(nmr1, nmr2 + 1, 1) :  # ! '+ 1' para incluir o nmr final na soma!
        soma += cont
    return soma

# ! Primeira Digitação dos Números
nmr1 = int(input("Digite o 1° valor: "))
nmr2 = int(input("Digite o 2° valor: "))

# ! Chamada das Funções
nmr1, nmr2 = validarInteiro(nmr1, nmr2)
print(f"A soma dos números entre {nmr1} e {nmr2} é igual a: {somarNumeros(nmr1, nmr2)}")
