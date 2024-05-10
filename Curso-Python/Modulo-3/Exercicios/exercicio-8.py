valor = 0
qtd = 0
for cont in range (1, 101, 1) :
    if (cont % 2 == 0) :
        valor += cont
        qtd += 1
media = valor / qtd
print(f"A média dos pares é: {media}")
