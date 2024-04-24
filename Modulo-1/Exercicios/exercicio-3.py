prcInici = float(input("Digite o preço inicial do produto \n"))
desconto = float(input("Digite o valor percentual do desconto \n"))

valorDoDesconto = prcInici / desconto
prcFinal = prcInici - valorDoDesconto

print(f"O preço após aplicado o desconto de {desconto}% ficou em: R${prcFinal}")
