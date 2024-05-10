print("Números primos de 2 a 100:")
for cont in range(2, 101):
    for cont2 in range(2, cont):
        if (cont % cont2) == 0:
            break
    else:
        print(cont, end=" ")
