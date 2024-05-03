lista = [23, 45, 3425, 3, 23, 0]
maiorNumero = lista[0]

for cont in lista :
    if (cont > maiorNumero) :
        maiorNumero = cont
    
print(f"O maior número da lista é: {maiorNumero}")
