ld1 = float(input("Entre com o valor do 1° lado: \n"))
ld2 = float(input("Entre com o valor do 2° lado: \n"))
ld3 = float(input("Entre com o valor do 3° lado: \n"))

if (ld1 <= 0) or (ld2 <= 0) or (ld3 <= 0) :
    print(f"Esses valores não formam um triângulo!")

if (ld1 > ld2 + ld3) or (ld2 > ld1 + ld3) or (ld3 > ld1 + ld2) :
    print(f"Esses valores não formam um triângulo!")

if (ld1 == ld2) and (ld1 == ld3) :
    print("Triângulo Equilátero")

elif (ld1 == ld2) or (ld1 == ld3) or (ld2 == ld3) :
    print("Triângulo Isóceles")

elif (ld1 != ld2) and (ld1 != ld3) and (ld2 != ld3):
    print("Triângulo Escaleno")
